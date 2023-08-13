from typing import Union

from routers import evento
 
from fastapi import FastAPI

app = FastAPI()

app.include_router(evento.router)