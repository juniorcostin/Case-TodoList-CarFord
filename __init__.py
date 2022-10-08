from api.modulos.usuarios import Usuarios
from api.configuracoes.configuracoes import db

def primeiro_usuario():
    try:
        admin = Usuarios(
                        nome="admin",
                        email="admin@admin.com",
                        senha="boladegordura",
                        admin=True
                    )
        db.session.add(admin)
        db.session.commit()

        viewer = Usuarios(
                        nome="viewer",
                        email="viewer@viewer.com",
                        senha="viewer@viewer.com",
                        admin=False
                    )
        db.session.add(admin)
        db.session.commit()
        db.session.add(viewer)
        db.session.commit()
        print("Usuario criado com sucesso!")
    except Exception as e:
        print(f'Falha ao criar usuário! Mensagem: {e}')

primeiro_usuario()