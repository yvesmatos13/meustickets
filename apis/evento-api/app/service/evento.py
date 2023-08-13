from fastapi import APIRouter, HTTPException
from schemas.evento import Evento, Evento_Update
from persistence.mongodb import connection, sequences
from pymongo import ReturnDocument

async def criar_evento(evento: Evento):
    evento = evento.dict()
    evento["id"] = await gerarId()
    connection().insert_one({"_id":evento["id"],"nome":evento["nome"],"tipo":evento["tipo"]})
    return evento

async def gerarId():
    return sequences().find_one_and_update(
        {'collection': 'evento_collection'},
        {'$inc': {'id': 1}},
        {'id': 1, '_id': 0}
    ).get('id')+1

async def buscar_eventos():
    eventos = []
    for evento in connection().find():
        evento = {"id":evento["_id"],
                  "nome":evento["nome"],
                  "tipo":evento["tipo"]}
        eventos.append(evento)
    return eventos

async def buscar_evento(evento_id: int):
    evento = connection().find_one({"_id":evento_id})
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    evento = {"id":evento["_id"],
                  "nome":evento["nome"],
                  "tipo":evento["tipo"]}
    return evento

async def editar_evento(evento: Evento_Update):
    evento = evento.dict()
    if not await buscar_evento(evento['id']):
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    evento = connection().find_one_and_update(
       {'_id': evento["id"]},
       {'$set':{'nome':evento["nome"],'tipo':evento["tipo"]}},
       return_document=ReturnDocument.AFTER
    )
    return {"id":evento["_id"],
                  "nome":evento["nome"],
                  "tipo":evento["tipo"]}

async def deletar_evento(evento_id: int):
    if not await buscar_evento(evento_id):
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    connection().delete_one({"_id":evento_id})
    return {"detail":"Evento deletado com sucesso"}