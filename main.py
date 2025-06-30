from fastapi import FastAPI
from typing import List
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Lotto ML+ API działa poprawnie"}

@app.get("/zaklad")
def generuj_zaklad():
    return {"zakład": sorted(random.sample(range(1, 50), 6))}

@app.get("/zaklady_ml")
def wiele_zakladow(ilosc: int = 10):
    return {"zakłady": [sorted(random.sample(range(1, 50), 6)) for _ in range(ilosc)]}
