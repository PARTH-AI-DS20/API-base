from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read():
    return {"status":"active"}
