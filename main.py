from model import chads_vasc_score

# Import FastAPI
from fastapi import FastAPI

# Instantiate App
app = FastAPI()

# Decorate Function
@app.get("/")
def run(age: int = 65, female: bool = True, chf: bool = False, hypertension: bool = False, stroke_tia: bool = False, vascular_disease: bool = False, diabetes: bool = False) -> str:
    return chads_vasc_score(age=age, 
                    female=female, 
                    chf=chf, 
                    hypertension=hypertension,
                    stroke_tia=stroke_tia, 
                    vascular_disease=vascular_disease, 
                    diabetes=diabetes)