from fastapi import FastAPI

app = FastAPI()

print("App started")

@app.get("/")
async def root():
    return {"message": "Hello World"}