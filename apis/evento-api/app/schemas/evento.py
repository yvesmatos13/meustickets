from pydantic import BaseModel

class Evento(BaseModel):
    nome: str
    tipo: str

class Evento_Update(BaseModel):
    id: int
    nome: str
    tipo: str

class Evento_Response(BaseModel):
    id: int
    nome: str
    tipo: str