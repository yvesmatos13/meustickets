from pydantic import BaseModel
from typing import Optional

class Excecao_Negocio(BaseModel):
    codigo: int
    mensagem: str

class Excecao_Infra_Estrutura(BaseModel):
    codigo: int
    mensagem: str

def excecao_negocio(mensagem: str):
    Excecao_Negocio.codigo = 400
    Excecao_Negocio.mensagem = mensagem

def excecao_infraEstrutura_timeout():
    Excecao_Infra_Estrutura.codigo = 504
    Excecao_Infra_Estrutura.mensagem = "Timeout"

def excecao_infraEstrutura():
    Excecao_Infra_Estrutura.codigo = 500
    Excecao_Infra_Estrutura.mensagem = "Entre em contato com o administrador"