# python -m uvicorn main:app --re
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

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

# Маршрут для получения всех карт
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

@app.get("/hr-insights")
def get_hr_insight(db: Session = Depends(get_db)):
    cards = db.query(models.TarotHRInsights).all()
    return cards
