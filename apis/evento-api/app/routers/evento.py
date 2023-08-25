from fastapi import APIRouter, HTTPException

import service.evento as eventoServico
from schemas.evento import Evento_Request, Evento_Update_Request, Evento_Response, Evento_Delete_Response
from schemas.excecoes import Excecao_Negocio, Excecao_Infra_Estrutura

class evento():

    router = APIRouter(
        prefix="/api/v1",
        tags=["eventos"],
        responses= {
            400: {"model": Excecao_Negocio, "description": "Exceção de negócio"},
            500: {"model": Excecao_Infra_Estrutura, "description": "Exceção de infra estrutura"},
            }
    )
    
    @router.post("/evento", response_model=Evento_Response, status_code=200)
    async def criar_evento(evento: Evento_Request):
        return await eventoServico.criar_evento(evento)
    
    @router.get("/eventos", response_model=list[Evento_Response], status_code=200)
    async def buscar_eventos():
        return await eventoServico.buscar_eventos()
    
    @router.get("/evento/{evento_id}", response_model=Evento_Response, status_code=200)
    async def buscar_evento(evento_id: int):
        return await eventoServico.buscar_evento(evento_id)
    
    @router.put("/evento/editar", response_model=Evento_Response, status_code=200)
    async def editar_evento(evento: Evento_Update_Request):
        return await eventoServico.editar_evento(evento)
    
    @router.delete("/evento/{evento_id}", response_model=Evento_Delete_Response, status_code=200)
    async def deletar_evento(evento_id: int):
        return await eventoServico.deletar_evento(evento_id)