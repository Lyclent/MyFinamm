from django.db import models
from django.db import models
from core.models import TimeStampedModel, OwnedModel
from accounts.models import Account
from categories.models import Category
from django.utils import timezone


class Transaction(TimeStampedModel, OwnedModel):
    TYPE_CHOICES = (
        ("income", "Income"),
        ("expense", "Expense"),
        ("transfer", "Transfer"),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    to_account = models.ForeignKey(
        Account,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="incoming_transfers"
    )

    amount = models.DecimalField(max_digits=14, decimal_places=2)

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    description = models.TextField(blank=True)

    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.type} {self.amount}"