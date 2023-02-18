from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Hello World"}

@app.get("/countries/{country_name}")
async def contry(country_name):
  return {"country_name": country_name}