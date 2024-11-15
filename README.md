# Open API для получения карт Таро

## Локальный запуск

### Установка Python

Для запуска нужен Python 3.7 или выше. Чтобы проверить наличие Python, выполните команду:

```
python3 --version
```

### Установка PostgreSQL

Для работы с базой данных PostgreSQL на сервере, вам нужно установить сам PostgreSQL.

```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

После установки PostgreSQL, запустите его:

```
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Создание базы данных

Теперь создайте базу данных с помощью PostgreSQL.
```
sudo -u postgres psql
CREATE DATABASE tarot_db;
CREATE USER tarot_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE tarot_db TO tarot_user;
\q
```

### Установка зависимостей

```
cd /path/to/your/project
python3 -m venv venv
pip install -r requirements.txt
```

### Установка переменных окружения

Создайте файл .env в корневой директории проекта и добавьте туда данные для подключения к базе данных:

```
DATABASE_URL=postgresql://tarot_user:your_password@localhost:5432/tarot_db
DB_HOST=localhost
DB_PORT=5432
DB_USER=tarot_user
DB_PASSWORD=your_password
DB_NAME=tarot_db
```

### Запуск скрипта для создания базы данных и таблиц

Теперь, когда все зависимости установлены и база данных создана, запустите скрипт create_db.py, чтобы создать таблицы на основе ваших SQL скриптов.

Запустите скрипт create_db.py:

```
python3 create_db.py
```

### Развертывание приложения

Теперь, когда база данных и таблицы созданы, можно развернуть приложение с FastAPI.

Запустите приложение с помощью Uvicorn:

```
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Перейдя по странице, можно увидеть документацию
http://localhost:8000/docs#
