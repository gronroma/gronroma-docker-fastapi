from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello local docker!", "v": "0.5" }

@app.get("/api/ip")
def ip(request: Request):
    return {"ip": request.client.host}

@app.get("/hello")
def hello():
    return {"msg": "Hello, böö!"}
