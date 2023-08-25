from pydantic import BaseModel, Field
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
    hora_inicio: time = Field(example="12:30")
    data_fim: date
    hora_fim: time = Field(example="12:30")

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
    hora_inicio: time = Field(example="12:30")
    data_fim: date
    hora_fim: time = Field(example="12:30")

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

class Evento_Delete_Response(BaseModel):
      codigo: int = 0
      mensagem: str = "Evento deletado com sucesso"

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