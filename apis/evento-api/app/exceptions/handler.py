from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from schemas.handler import Excecao_Negocio, Excecao_Infra_Estrutura

class ExcecaoNegocioException(HTTPException):
    pass

class ExcecaoInfraEstruturaException(HTTPException):
    pass

class ExcecaoInfraEstruturaTimeoutException(HTTPException):
    pass

def negocio_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"codigo": Excecao_Negocio.codigo, "mensagem":Excecao_Negocio.mensagem})

def infraEstrutura_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"codigo": Excecao_Infra_Estrutura.codigo, "mensagem":Excecao_Infra_Estrutura.mensagem})

def timeout_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=status.HTTP_504_GATEWAY_TIMEOUT, content={"codigo": Excecao_Infra_Estrutura.codigo, "mensagem":Excecao_Infra_Estrutura.mensagem})