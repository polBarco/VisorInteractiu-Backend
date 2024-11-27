from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import Cartography, d50, LitoralCells, CycloneSedimentTransport, CycloneEra5Node, Rivers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Cartography.router)
app.include_router(d50.router)
app.include_router(LitoralCells.router)
app.include_router(CycloneSedimentTransport.router)
app.include_router(CycloneEra5Node.router)
app.include_router(Rivers.router)