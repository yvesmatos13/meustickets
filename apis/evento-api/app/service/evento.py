from fastapi import APIRouter, HTTPException
from schemas.evento import Evento, Evento_Update
from schemas.excecoes import excecao_negocio, excecao_infraEstrutura, excecao_infraEstrutura_timeout
from persistence.mongodb import connection, sequences
from exceptions.handler import ExcecaoNegocioException, ExcecaoInfraEstruturaException, ExcecaoInfraEstruturaTimeoutException

async def criar_evento(evento: Evento):
    evento = evento.dict()
    evento["_id"] = await gerarId()
    try:
        evento = connection().insert_one(evento)
    
    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)
    return await buscar_evento(evento.inserted_id)        

async def gerarId():
    try:
        return sequences().find_one_and_update(
            {'collection': 'evento_collection'},
            {'$inc': {'id': 1}},
            {'id': 1, '_id': 0}
        ).get('id')+1
    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)        

async def buscar_eventos():
    try:
        eventos = []
        for evento in connection().find():
            evento["id"] = evento.pop("_id")
            id = {'id': evento["id"]}
            evento = {**id, **evento}
            eventos.append(evento)

        return eventos
    
    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)        

async def buscar_evento(evento_id: int):
    try:
        evento = connection().find_one({"_id": evento_id})

    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)

    if not evento:
        excecao_negocio("Evento não encontado")
        raise ExcecaoNegocioException(status_code=400)
    evento["id"] = evento.pop("_id")
    id = {'id': evento["id"]}
    evento = {**id, **evento}
    return evento

async def editar_evento(evento: Evento_Update):
    evento = evento.dict()
    await buscar_evento(evento['id'])
    try:    
        connection().find_one_and_update(
            {'_id': evento["id"]},
            {'$set': evento}
        )
    
    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)        
    return await buscar_evento(evento['id'])

async def deletar_evento(evento_id: int):
    await buscar_evento(evento_id)
    try:
        connection().delete_one({"_id": evento_id})

        return {"detail": "Evento deletado com sucesso"}
    
    except Exception as e:
        excecao = str(e.args)
        print(excecao)
        excecao_infraEstrutura()
        if excecao.find("Timeout") > -1 or excecao.find("timeout") > -1 or excecao.find("Time-out") > -1 or excecao.find("time-out") > -1 or excecao.find("time out") > -1 or excecao.find("Time out") > -1:
            excecao_infraEstrutura_timeout()
            ExcecaoInfraEstruturaTimeoutException(status_code=504)
        raise ExcecaoInfraEstruturaException(status_code=500)        

