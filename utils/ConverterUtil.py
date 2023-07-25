class ConverterUtil:
    def usuario_converter(self, usuario):
        return {
            "id": str(usuario["_id"]),
            "nome": str(usuario["nome"]),
            "email": str(usuario["email"]),
            "senha": str(usuario["senha"]),
            "foto": str(usuario["foto"]) if "foto" in usuario else ""
        }

    def postagem_converter(self, postagem):
        return {
            "id": str(postagem["_id"]) if "_id" in postagem else "",
            "usuario": postagem["usuario"] if "usuario" in postagem else "",
            "foto": postagem["foto"] if "foto" in postagem else "",
            "legenda": postagem["legenda"] if "legenda" in postagem else "",
            "data": postagem["data"] if "data" in postagem else "",
            "curtidas": postagem["comentarios"] if "comentarios" in postagem else ""

        }
