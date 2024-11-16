# python -m uvicorn main:app --re
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging
from datetime import datetime
from typing import List
from pydantic import BaseModel

import models
import db

# Инициализация приложения
app = FastAPI()

# Включить логирование для SQLAlchemy
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# Функция для получения сессии базы данных
def get_db():
    db_session = db.SessionLocal()  # Изменено с `db` на `db_session`
    try:
        yield db_session
    finally:
        db_session.close()

# Создание таблиц в базе данных
models.Base.metadata.create_all(bind=db.engine)

# Маршрут для получения карты по ID
@app.get("/cards/{id}")
def get_card(id: int, db: Session = Depends(get_db)):
    if not (1 <= id <= 22):
        raise HTTPException(status_code=404, detail="Card not found")
    card = db.query(models.MajorArcana).filter(models.MajorArcana.id == id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

# Маршрут для получения всех карт MajorArcana
@app.get("/cards")
def get_all_cards(db: Session = Depends(get_db)):
    cards = db.query(models.MajorArcana).all()
    return cards

# Маршрут для получения hr-инсайта по ID
@app.get("/hr-insights/{id}")
def get_hr_insight(id: int, db: Session = Depends(get_db)):
    if not (1 <= id <= 22):
        raise HTTPException(status_code=404, detail="Card not found")
    insight = db.query(models.TarotHRInsights).filter(models.TarotHRInsights.id == id).first()
    if not insight:
        raise HTTPException(status_code=404, detail="HR insight not found")
    return insight

# Маршрут для получения всех карт TarotHRInsights
@app.get("/hr-insights")
def get_hr_insight(db: Session = Depends(get_db)):
    cards = db.query(models.TarotHRInsights).all()
    return cards

def validate_and_sum_date(date_str: str) -> int:
    try:
        # Попробуем преобразовать строку в дату
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        
        # Получаем строковое представление даты (например, "15.11.2024")
        date_digits = date_str.replace('.', '')  # Убираем точки, оставляем только цифры
        
        # Считаем сумму всех цифр
        digit_sum = sum(int(digit) for digit in date_digits)
        
        # Если сумма больше 22, применяем операцию взятия остатка, чтобы результат был в диапазоне 1..22
        if digit_sum > 22:
            digit_sum = (digit_sum - 1) % 22 + 1
        
        return digit_sum
    
    except ValueError:
        # Если произошла ошибка преобразования, значит дата некорректна
        return -1  # Можно вернуть любое значение, например, -1, чтобы указать на ошибку

# Маршрут для получения карты по дате рождения
@app.get("/arcane/{birth_date}")
def get_arcane(birth_date: str, db: Session = Depends(get_db)):
    arcane = validate_and_sum_date(birth_date)
    if arcane == -1:
        raise HTTPException(status_code=400, detail="Bad request. Syntax error in birth_date")
    card = db.query(models.MajorArcana).filter(models.MajorArcana.id == arcane).first()
    if not card:
        raise HTTPException(status_code=404, detail=f"Card not found, ID Card: {arcane}")
    return card

# Маршрут для hr-инсайта по дате рождения
@app.get("/arcane-candidate/{birth_date}")
def get_arcane_candidate(birth_date: str, db: Session = Depends(get_db)):
    arcane = validate_and_sum_date(birth_date)
    if arcane == -1:
        raise HTTPException(status_code=400, detail="Bad request. Syntax error in birth_date")
    card = db.query(models.TarotHRInsights).filter(models.TarotHRInsights.id == arcane).first()
    if not card:
        raise HTTPException(status_code=404, detail=f"Card not found, ID Card: {arcane}")
    return card

# Функция для обработки списка дат
def validate_and_sum_dates(birth_dates: List[str]) -> int:
    total_sum = 0
    for birth_date in birth_dates:
        result = validate_and_sum_date(birth_date)
        if result == -1:
            raise HTTPException(status_code=400, detail=f"Invalid date format: {birth_date}")
        total_sum += result
    
    # Если сумма всех результатов больше 22, применяем операцию взятия остатка
    total_sum = (total_sum - 1) % 22 + 1
    return total_sum


class BirthDatesRequest(BaseModel):
    birth_dates: List[str]

# Маршрут для описания отношений в коллективе по датам рождения людей в коллективе
@app.post("/arcane-group")
def get_arcane_candidate(request: BirthDatesRequest, db: Session = Depends(get_db)):
    arcane = validate_and_sum_dates(request.birth_dates)
    if arcane == -1:
        raise HTTPException(status_code=400, detail="Bad request. Syntax error in dates")
    card = db.query(models.TarotHRGroupInsights).filter(models.TarotHRGroupInsights.id == arcane).first()
    if not card:
        raise HTTPException(status_code=404, detail=f"Card not found, ID Card: {arcane}")
    return card

# Маршрут для получения всех карт TarotHRGroupInsights
@app.get("/arcane-group")
def get_arcane_candidate(db: Session = Depends(get_db)):
    cards = db.query(models.TarotHRGroupInsights).all()
    return cards
    
