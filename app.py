from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{name}")
async def home(name):
    return {"Your name is": name}

@app.get("/num/{num}")
async def home(num:int):
    return {"Your lucky number is": num}