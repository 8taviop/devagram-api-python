from fastapi import Form, UploadFile
from pydantic import BaseModel, Field, EmailStr
from utils.DecoratorUtil import DecoratorUtil

decoratorUtil = DecoratorUtil()


class UsuarioModel(BaseModel):
    id: str = Field(...)
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "Senha123!",
                "foto": "fulano.jpg"
            }
        }


@decoratorUtil.form_body
class UsuarioCriarModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "Senha123!"
            }
        }


class UsuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "email": "fulano@gmail.com",
                "senha": "Senha123!",
            }
        }


@decoratorUtil.form_body
class UsuarioAtualizarModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: UploadFile = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "Senha123!"
            }
        }
