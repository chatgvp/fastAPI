from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    appshit = {"Hello": "World"}
    print(appshit)
    return appshit


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/add/{num1}/{num2}")
def add_numbers(num1: float, num2: float):
    return {"result": num1 + num2}


@app.get("/subtract/{num1}/{num2}")
def subtract_numbers(num1: float, num2: float):
    return {"result": num1 - num2}


@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(num1: float, num2: float):
    return {"result": num1 * num2}


@app.get("/divide/{num1}/{num2}")
def divide_numbers(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": num1 / num2}
