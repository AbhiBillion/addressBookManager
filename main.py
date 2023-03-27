from fastapi import FastAPI
from routes.dbRoutes import user

app = FastAPI()

app.include_router(user.routes)