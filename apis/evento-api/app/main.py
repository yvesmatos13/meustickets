from typing import Union

import routers.evento as evento
 
from fastapi import FastAPI

from exceptions.handler import ExcecaoInfraEstruturaException, ExcecaoNegocioException, negocio_exception_handler, infraEstrutura_exception_handler

app = FastAPI()

app.include_router(evento.router)
app.add_exception_handler(ExcecaoNegocioException, negocio_exception_handler)
app.add_exception_handler(ExcecaoInfraEstruturaException, infraEstrutura_exception_handler)