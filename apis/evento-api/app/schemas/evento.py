from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class Evento(BaseModel):
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

class Evento_Update(BaseModel):
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