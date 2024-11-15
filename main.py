from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import Cartography, d50

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # La URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Cartography.router)
app.include_router(d50.router)