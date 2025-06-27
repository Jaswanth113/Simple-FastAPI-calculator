from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def addition(a: float, b:float):
    result = a + b
    return(result)

@app.get("/subtraction")
def subtraction(a: float, b: float):
    result = a - b
    return(result)

@app.get("/multiplication")
def multiplication(a:float, b:float):
    result = a * b
    return(result)

@app.get("/division")
def division(a:float, b:float):
    if b == 0:
        return("cannot be divided by zero")
    result = a/b
    return(result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app")
