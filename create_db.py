import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
# Получаем данные из переменных окружения
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")  # Укажите свой пароль
DB_NAME = os.getenv("DB_NAME", "tarot_db")

# Путь к папке, содержащей SQL скрипты
DB_SQL_PATH = os.path.join(os.path.dirname(__file__), "db_sql")

# Путь к SQL скриптам
MAJOR_ARCANA_SQL = os.path.join(DB_SQL_PATH, "major_arcana.sql")
TAROT_HR_INSIGHTS_SQL = os.path.join(DB_SQL_PATH, "tarot_hr_insights.sql")
TAROT_HR_GROUP_INSIGHTS_SQL = os.path.join(DB_SQL_PATH, "tarot_group_insights.sql")

def execute_sql_script(cursor, table_name, sql_insert):
    """Функция для вставки данных в таблицу, если в ней меньше 22 записей"""
    cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
    print(f"Таблица {table_name} успешно удалена.")

    try:
        cursor.execute(sql_insert)
        print(f"Таблица {table_name} успешно создана.")
        
        # Сбрасываем последовательность для нового значения id
        cursor.execute(f"""
            SELECT setval('{table_name}_id_seq', COALESCE((SELECT MAX(id) FROM {table_name}), 1), false);
        """)
        print(f"Последовательность для {table_name}_id_seq сброшена на правильное значение.")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта для таблицы {table_name}: {e}")

# Соединяемся с сервером PostgreSQL
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    connection.autocommit = True  # Включаем автофиксацию изменений
    cursor = connection.cursor()

    # Создаем базу данных, если она не существует
    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()
    if not exists:
        print(f"Создаю базу данных: {DB_NAME}")
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
    else:
        print(f"База данных {DB_NAME} уже существует")

    # После создания базы данных подключаемся к ней и выполняем SQL скрипты
    cursor.execute("SELECT current_database();")
    print(f"Текущая база данных: {cursor.fetchone()[0]}")

    # Выполняем SQL скрипты
    with open(MAJOR_ARCANA_SQL, 'r', encoding='utf-8') as file:
        sql_insert = file.read()
    print(f"Выполняю скрипт {MAJOR_ARCANA_SQL} для создания таблиц Major Arcana")
    execute_sql_script(cursor, 'major_arcana', sql_insert)
    connection.commit()

    with open(TAROT_HR_INSIGHTS_SQL, 'r', encoding='utf-8') as file:
        sql_insert = file.read()
    print(f"Выполняю скрипт {TAROT_HR_INSIGHTS_SQL} для создания таблиц Tarot HR Insights")
    execute_sql_script(cursor, 'tarot_hr_insights', sql_insert)
    connection.commit()

    with open(TAROT_HR_GROUP_INSIGHTS_SQL, 'r', encoding='utf-8') as file:
            sql_insert = file.read()
    print(f"Выполняю скрипт {TAROT_HR_GROUP_INSIGHTS_SQL} для создания таблиц Tarot HR Group Insights")
    execute_sql_script(cursor, 'tarot_group_insights', sql_insert)
    connection.commit()

    # Закрываем курсор и соединение
    cursor.close()
    connection.close()
    
    print("База данных и таблицы успешно созданы и заполнены!")

except Exception as error:
    print(f"Ошибка при подключении к PostgreSQL: {error}")
