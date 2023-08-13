from fastapi import APIRouter, HTTPException

from service import evento as eventoServico
from schemas.evento import Evento, Evento_Update

router = APIRouter(
    #prefix="/eventos",
    tags=["eventos"],
    responses={404: {"description": "Not found"}},
)

@router.post("/evento")
async def criar_evento(evento: Evento):
    return await eventoServico.criar_evento(evento)

@router.get("/eventos")
async def buscar_eventos():
    return await eventoServico.buscar_eventos()

@router.get("/evento/{evento_id}")
async def buscar_evento(evento_id: int):
    return await eventoServico.buscar_evento(evento_id)

@router.put("/evento/editar")
async def editar_evento(evento: Evento_Update):
    return await eventoServico.editar_evento(evento)

@router.delete("/evento/{evento_id}", status_code=200)
async def deletar_evento(evento_id: int):
    return await eventoServico.deletar_evento(evento_id)