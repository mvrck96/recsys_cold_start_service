from fastapi import FastAPI
from loguru import logger
from os import getenv
from dotenv import dotenv_values

import sys
sys.path.append("./src")

from data_models import PredictData
import clustering

app = FastAPI()
logger.info(f"API started")

# Предполагаемая логика запросов такая, есть фит на полученных данных
# Есть предикт холодных на ALS есть предикт с помощью кластеризации
# Возвращает на предикт топ N самых близких обьектов
# На вход фита отдаем csv или parquet с матрицей покупок СТАНДАРТИЗИРОВАННЫЙ
# В предикт отдаем представление пользователя и Н обьектов для предсказания 

@app.post("/als_fit")
def fit():
    return "als predict"


@app.post("/als_predict")
def predict(PredictData):
    return {"mode": "predict"}

