from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
   return {"Hello": "World"}

@app.post("/")
async def create_user():
   ...
