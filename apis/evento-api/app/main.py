from typing import Union

from persitencia.conexao import conexao

from routers import evento
 
from fastapi import FastAPI

app = FastAPI()

app.include_router(evento.router)