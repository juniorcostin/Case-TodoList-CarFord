from modulos.usuarios import Usuarios
from modulos.carros import Carros
from modulos.proprietarios import Proprietarios
from configuracoes.configuracoes import db
import time

tabelas_criadas = False

while tabelas_criadas == False:
    try:
        db.create_all()
        print("tabelas criadas com sucesso!")
        tabelas_criadas = True
    except Exception as e:
        print("Falha ao criar tabelas, tentando novamente!")
        print("Caso o erro continue valide se o banco de dados subiu")
        print("AGUARDE")
        print("erro:", e)
        time.sleep(10)
        

def primeiro_usuario():
    try:
        admin = Usuarios(
                        nome="admin",
                        email="admin@admin.com",
                        senha="admin",
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