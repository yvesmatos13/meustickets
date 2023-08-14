from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class Evento_Request(BaseModel):
    nome: str
    tipo: str
    cep: str
    endereco: str
    numero: str
    complemento: str = None
    bairro: str
    cidade: str
    uf: str
    imagem: bytes = None
    assunto: str
    categoria: str = None
    descricao: str = None
    data_inicio: date
    hora_inicio: time
    data_fim: date
    hora_fim: time

class Evento_Update_Request(BaseModel):
    id: int
    nome: str
    tipo: str
    cep: str
    endereco: str
    numero: str
    complemento: str = None
    bairro: str
    cidade: str
    uf: str
    imagem: bytes = None
    assunto: str
    categoria: str = None
    descricao: str = None
    data_inicio: date
    hora_inicio: time
    data_fim: date
    hora_fim: time

class Evento_Response(BaseModel):
    id: int
    nome: str
    tipo: str
    cep: str
    endereco: str
    numero: str
    complemento: str = None
    bairro: str
    cidade: str
    uf: str
    imagem: bytes = None
    assunto: str
    categoria: str = None
    descricao: str = None
    data_inicio: date
    hora_inicio: time
    data_fim: date
    hora_fim: time

def evento_request(evento: Evento_Request):
        evento["data_inicio"] = str(evento["data_inicio"])
        evento["hora_inicio"] = str(evento["hora_inicio"])
        evento["data_fim"] = str(evento["data_fim"])
        evento["hora_fim"] = str(evento["hora_fim"])
        return evento

def evento_update_request(evento: Evento_Update_Request):
        evento["data_inicio"] = str(evento["data_inicio"])
        evento["hora_inicio"] = str(evento["hora_inicio"])
        evento["data_fim"] = str(evento["data_fim"])
        evento["hora_fim"] = str(evento["hora_fim"])
        return evento