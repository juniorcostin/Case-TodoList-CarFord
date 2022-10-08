from api.modulos.usuarios import Usuarios
from api.configuracoes.configuracoes import db

def primeiro_usuario():
    try:
        usuario = Usuarios(
                        nome="admin",
                        email="admin@admin.com",
                        senha="boladegordura",
                        admin=True
                    )
        db.session.add(usuario)
        db.session.commit()
        print("Usuario criado com sucesso!")
    except Exception as e:
        print(f'Falha ao criar usuário! Mensagem: {e}')

primeiro_usuario()