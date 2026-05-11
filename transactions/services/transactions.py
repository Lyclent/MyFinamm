from decimal import Decimal
from django.db import transaction as db_transaction
from django.core.exceptions import ValidationError
from django.db.models import Sum
from transactions.models import Transaction
from goals.models import Goal
from accounts.models import Account
from transactions.models import Transaction
from subscriptions.models import Subscription
from datetime import timedelta


@db_transaction.atomic
def create_transaction(user, **data):
    account = data.get("account")
    amount = Decimal(data.get("amount"))
    tx_type = data.get("type")

    if amount <= 0:
        raise ValidationError("Amount must be positive")

    if account.user != user:
        raise ValidationError("Invalid account")

    if tx_type == "expense" and account.balance < amount:
        raise ValidationError("Insufficient funds")

    transaction = Transaction.objects.create(user=user, **data)

    if tx_type == "expense":
        account.balance -= amount

    elif tx_type == "income":
        account.balance += amount

    elif tx_type == "transfer":
        to_account = data.get("to_account")

        if not to_account:
            raise ValidationError("Transfer requires to_account")

        if to_account.user != user:
            raise ValidationError("Invalid target account")

        if account.balance < amount:
            raise ValidationError("Insufficient funds")

        account.balance -= amount
        to_account.balance += amount

        to_account.save()

    account.save()

    return transaction

@db_transaction.atomic
def transfer_money(user, from_account, to_account, amount):
    amount = Decimal(amount)

    if amount <= 0:
        raise ValidationError("Amount must be positive")

    if from_account.user != user or to_account.user != user:
        raise ValidationError("Invalid accounts")

    if from_account.id == to_account.id:
        raise ValidationError("Cannot transfer to same account")

    if from_account.balance < amount:
        raise ValidationError("Insufficient funds")

    from_account.balance -= amount
    to_account.balance += amount

    from_account.save()
    to_account.save()

    return Transaction.objects.create(
        user=user,
        type="transfer",
        account=from_account,
        to_account=to_account,
        amount=amount
    )

@db_transaction.atomic
def apply_subscription(subscription):
    account = subscription.account

    if not subscription.is_active:
        return None

    if account.balance < subscription.amount:
        raise ValidationError("Not enough money for subscription")

    account.balance -= subscription.amount
    account.save()

    tx = Transaction.objects.create(
        user=subscription.user,
        type="expense",
        account=account,
        amount=subscription.amount,
        category=subscription.category,
        description=f"Subscription: {subscription.name}"
    )

    if subscription.period == "monthly":
        subscription.next_payment_date += timedelta(days=30)
    elif subscription.period == "yearly":
        subscription.next_payment_date += timedelta(days=365)

    subscription.save()

    return tx


def check_budget_limit(user, category, start_date, end_date, limit):
    total = (
        Transaction.objects.filter(
            user=user,
            category=category,
            type="expense",
            date__range=(start_date, end_date)
        )
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    return total > limit


@db_transaction.atomic
def add_money_to_goal(goal, amount):
    amount = Decimal(amount)

    if amount <= 0:
        raise ValidationError("Amount must be positive")

    goal.current_amount += amount

    if goal.current_amount >= goal.target_amount:
        goal.is_completed = True

    goal.save()

    return goal