import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
# Подключение к базе данных PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:3009@localhost:5432/tarot_db")
engine = create_engine(DATABASE_URL)

# Базовый класс для создания моделей
Base = declarative_base()

def initialize_database():
    with engine.connect() as connection:
        # Выполнение SQL скриптов для создания таблиц
        with connection.begin():
            try:
                # major_arcana.sql
                connection.execute(text("""
                    CREATE TABLE IF NOT EXISTS major_arcana (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT NOT NULL,
                    relationship_interpretation TEXT NOT NULL,
                    career_interpretation TEXT NOT NULL
                );
                """))

                # tarot_hr_insights.sql
                connection.execute(text("""
                    CREATE TABLE IF NOT EXISTS tarot_hr_insights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    workplace_relationship_interpretation TEXT NOT NULL,
    career_interpretation TEXT NOT NULL
);

                """))

                print("Таблицы успешно созданы.")
            except Exception as e:
                print("Произошла ошибка при создании таблиц:", e)

# Настроить сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
