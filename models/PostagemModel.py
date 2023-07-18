from pydantic import BaseModel, Field
from typing import List

from models import ComentarioModel
from models.UsuarioModel import UsuarioModel


class PostagemModel(BaseModel):
    id: str = Field(...)
    usuario: UsuarioModel = Field(...)
    foto: str = Field(...)
    legenda: str = Field(...)
    data: str = Field(...)
    curtidas: int = Field(...)
    comentarios: List[ComentarioModel] = Field(...)

    class Config:
        scheme_extra = {
            "postagem": {
                "id": "string",
                "foto": "string",
                "legenda": "string",
                "data": "string",
                "curtidas": "int",
                "comentarios": "List[comentarios]"
            }
        }


class PostagemCriarModel(BaseModel):
    usuario: UsuarioModel = Field(...)
    foto: str = Field(...)
    legenda: str = Field(...)

    class Config:
        scheme_extra = {
            "postagem": {
                "usuario": "UsuarioModel",
                "foto": "string",
                "legenda": "string"
            }
        }
