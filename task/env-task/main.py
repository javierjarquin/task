from fastapi import FastAPI
from route.routes import task
app = FastAPI()

app.include_router(task)