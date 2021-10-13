from typing import List

from fastapi import FastAPI

import sys
sys.path.insert(1, 'api/ML')
from model import Model


class PredictRequest(Model):
    data: List[List[float]]


class PredictResponse(Model):
    data: List[float]


app = FastAPI()


@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest):
    return PredictResponse(data=[0.0])