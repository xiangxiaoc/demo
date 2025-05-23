from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"version": "v1", "message": "hello"}

