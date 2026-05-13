💰 MyFinam
MyFinam — это backend-приложение для личного учета финансов, разработанное на Django REST Framework.

Пользователь может:

управлять счетами,
отслеживать доходы и расходы,
создавать бюджеты,
контролировать подписки,
анализировать финансовую статистику.
Проект создан как учебное финтех-приложение с использованием современной backend-архитектуры.

🚀 Возможности
👤 Пользователи
JWT авторизация
Регистрация и аутентификация
Изоляция данных пользователей
💳 Accounts
Создание счетов
Баланс
Поддержка валют
💸 Transactions
Доходы
Расходы
Переводы между счетами
🏷 Categories
Категории доходов и расходов
📊 Budgets
Ограничения бюджета
Контроль расходов
🎯 Goals
Финансовые цели
Накопления
🔁 Subscriptions
Автоматические подписки
Проверка списаний
📈 Analytics API
Общий баланс
Доходы и расходы
Статистика по категориям
Расходы за месяц
🛠 Технологии
Python 3
Django
Django REST Framework
JWT Authentication
SQLite
ORM
DRF ViewSets
Services Layer Architecture
🧠 Архитектура проекта
Проект построен по принципу разделения ответственности:

Views → Services → Models
Структура:
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
Основные принципы:
бизнес-логика вынесена в services
API построен на DRF
аналитика реализована через APIView
JWT авторизация
тестирование ключевой логики
🔐 JWT Авторизация
Получение токена
POST:

/api/token/
Body:
{
    "username": "admin",
    "password": "password"
}
Response:
{
    "refresh": "...",
    "access": "..."
}
📡 API Endpoints
Accounts
/api/accounts/
Transactions
/api/transactions/
Categories
/api/categories/
Budgets
/api/budgets/
Goals
/api/goals/
Subscriptions
/api/subscriptions/
Analytics
Summary
/api/analytics/summary/
Monthly expenses
/api/analytics/monthly-expenses/
Top categories
/api/analytics/top-categories/
📊 Пример Analytics Response
{
    "income": 150000,
    "expenses": 70000,
    "balance": 80000
}
📌 Особенности проекта
Использование services layer
Финансовая бизнес-логика
JWT authentication
Analytics API
ORM aggregates
Изоляция данных пользователей
Покрытие тестами
