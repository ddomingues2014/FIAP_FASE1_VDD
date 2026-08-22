#python3 -m venv ./venv/

#source ./venv/bin/activate

# python3 -m pip install --upgrade pip

#pip install "fastapi[standard]"
#fastapi dev main.py

#pip install scikit-learn


from typing import Union
import pickle

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
#@app.post("/predict")
def make_predict(
    concave_points_mean,
    concave_points_worst,
    perimeter_worst,
    radius_worst
):
    
    model = pickle.load(open("modelo_pipeline.pkl", "rb"))

    novo_input = [[
        float(concave_points_mean),
        float(concave_points_worst),
        float(perimeter_worst),
        float(radius_worst)
    ]]

    _predict = model.predict(novo_input)
    _predict = str(_predict[0])


    return {
        "output": _predict
    }