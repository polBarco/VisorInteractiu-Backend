from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import Cartography, d50, LitoralCells, CycloneSedimentTransport, CycloneEra5Node, RiversMozambique , Hurricane

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://polbarco.github.io/VisorInteractiu-Frontend/", "localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Cartography.router)
app.include_router(d50.router)
app.include_router(LitoralCells.router)
app.include_router(CycloneSedimentTransport.router)
app.include_router(CycloneEra5Node.router)
app.include_router(RiversMozambique.router)
app.include_router(Hurricane.router)