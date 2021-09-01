import math
import uvicorn
import statistics
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

tags_metadata = [{
    "name": "calculator",
    "description": "Operações matemáticas simples.",
}, {
    "name": "calc_statistics",
    "description": "Operações matemáticas complexas.",
}]


class Calculator(BaseModel):
    operation: str = "somar"
    first_value: int = 2
    second_value: int = 2


class CalcStatistics(BaseModel):
    type: str = "moda"
    values: list = [1, 2, 5, 2, 23, 5, 2]


app = FastAPI(title="Calculadora API",
              version="0.1.0",
              openapi_tags=tags_metadata)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/calculator", tags=["calculator"])
async def calculator(calculator: Calculator):
    if calculator.operation == 'somar':
        return {"resultado": calculator.first_value + calculator.second_value}
    elif calculator.operation == 'subtrair':
        return {"resultado": calculator.first_value - calculator.second_value}
    elif calculator.operation == 'multiplicar':
        return {"resultado": calculator.first_value * calculator.second_value}
    elif calculator.operation == 'dividir':
        return {"resultado": calculator.first_value / calculator.second_value}
    elif calculator.operation == 'potencia':
        return {"resultado": calculator.first_value**calculator.second_value}
    elif calculator.operation == 'raiz':
        return {
            "resultado": {
                "raiz_a": math.sqrt(calculator.first_value),
                "raiz_b": math.sqrt(calculator.second_value)
            }
        }


@app.post("/api/v1/calculator/statistics", tags=["calc_statistics"])
async def calculator_statistics(calc_statistics: CalcStatistics):
    if calc_statistics.type == 'moda':
        return {"resultado": statistics.mode(calc_statistics.values)}

    total = 0
    length = len(calc_statistics.values)

    if calc_statistics.type == 'media':
        for x in calc_statistics.values:
            total += x

        return {"resultado": total / length}
    elif calc_statistics.type == 'harmonica':
        for x in calc_statistics.values:
            total += 1 / x

        return {"resultado": length / total}


uvicorn.run(app, host="0.0.0.0")
