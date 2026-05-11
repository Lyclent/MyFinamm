# 💰 MyFinam

MyFinam — это backend-приложение для личного учета финансов, разработанное на Django REST Framework.

Пользователь может:
- управлять счетами,
- отслеживать доходы и расходы,
- создавать бюджеты,
- контролировать подписки,
- анализировать финансовую статистику.

Проект создан как учебное финтех-приложение с использованием современной backend-архитектуры.

---

# 🚀 Возможности

## 👤 Пользователи
- JWT авторизация
- Регистрация и аутентификация
- Изоляция данных пользователей

## 💳 Accounts
- Создание счетов
- Баланс
- Поддержка валют

## 💸 Transactions
- Доходы
- Расходы
- Переводы между счетами

## 🏷 Categories
- Категории доходов и расходов

## 📊 Budgets
- Ограничения бюджета
- Контроль расходов

## 🎯 Goals
- Финансовые цели
- Накопления

## 🔁 Subscriptions
- Автоматические подписки
- Проверка списаний

## 📈 Analytics API
- Общий баланс
- Доходы и расходы
- Статистика по категориям
- Расходы за месяц

---

# 🛠 Технологии

- Python 3
- Django
- Django REST Framework
- JWT Authentication
- SQLite
- ORM
- DRF ViewSets
- Services Layer Architecture

---

# 🧠 Архитектура проекта

Проект построен по принципу разделения ответственности:

```text
Views → Services → Models
```

## Структура:

```text
accounts/
transactions/
budgets/
goals/
subscriptions/
analytics/
currency/
notifications/
categories/
users/
core/
```

### Основные принципы:
- бизнес-логика вынесена в services
- API построен на DRF
- аналитика реализована через APIView
- JWT авторизация
- тестирование ключевой логики

---

# 🔐 JWT Авторизация

## Получение токена

POST:

```text
/api/token/
```

### Body:

```json
{
    "username": "admin",
    "password": "password"
}
```

### Response:

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

# 📡 API Endpoints

## Accounts

```text
/api/accounts/
```

## Transactions

```text
/api/transactions/
```

## Categories

```text
/api/categories/
```

## Budgets

```text
/api/budgets/
```

## Goals

```text
/api/goals/
```

## Subscriptions

```text
/api/subscriptions/
```

## Analytics

### Summary

```text
/api/analytics/summary/
```

### Monthly expenses

```text
/api/analytics/monthly-expenses/
```

### Top categories

```text
/api/analytics/top-categories/
```

---

# 📊 Пример Analytics Response

```json
{
    "income": 150000,
    "expenses": 70000,
    "balance": 80000
}
```

---

# ⚙️ Установка проекта

## 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/myfinam.git
```

## 2. Переход в папку проекта

```bash
cd myfinam
```

## 3. Создание виртуального окружения

```bash
python -m venv venv
```

## 4. Активация venv

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Установка зависимостей

```bash
pip install -r requirements.txt
```

## 6. Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

## 7. Создание суперпользователя

```bash
python manage.py createsuperuser
```

## 8. Запуск сервера

```bash
python manage.py runserver
```

---

# 🧪 Тестирование

Запуск тестов:

```bash
python manage.py test
```

Тестируются:
- transactions services
- subscriptions
- JWT auth
- API permissions

---

# 📌 Особенности проекта

- Использование services layer
- Финансовая бизнес-логика
- JWT authentication
- Analytics API
- ORM aggregates
- Изоляция данных пользователей
- Покрытие тестами

---