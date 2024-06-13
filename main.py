from fastapi import FastAPI

app = FastAPI()
#swagger http://127.0.0.1:8000/docs
#example how to define a rute
@app.get("/")
def read_root():
    return {"Hello": "World"}


