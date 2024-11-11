from entity.usuario import Usuario  # Importando o modelo Usuario
from db import db

class UsuarioRepository:

    @staticmethod
    def get_all():
        # Retorna todos os usuários.
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id_usuario):
        # Retorna um usuário pelo ID
        return Usuario.query.get(id_usuario)
    
    @staticmethod
    def get_by_login(login):
        # Retorna um usuário pelo login
        return Usuario.query.filter_by(login=login).first()
    
    @staticmethod
    def get_by_perfil(perfil):
        # Retorna os usuários pelo perfil
        return Usuario.query.filter_by(perfil=perfil).all()

    @staticmethod
    def create(usuario):
        # Cria um novo usuário no banco de dados.
        try:
            # Consultar se já existe um usuário com o mesmo login
            existing_usuario = Usuario.query.filter_by(login=usuario.login).first()
            if existing_usuario:
                raise ValueError("Login já existe.")

            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao criar usuário: {e}")
            return None  # Retorna None em caso de falha

    @staticmethod
    def usuario_update(usuario):
        # Atualiza as informações de um usuário existente no banco de dados.
        try:
            existing_usuario = UsuarioRepository.get_by_id(usuario.id_usuario)
            if not existing_usuario:
                raise ValueError("Usuário não encontrado.")

            # Atualiza os campos do usuário
            existing_usuario.login = usuario.login
            existing_usuario.senha = usuario.senha
            existing_usuario.perfil = usuario.perfil
            # Adicione outros campos que precisam ser atualizados aqui

            db.session.commit()  # Salva as alterações
            return existing_usuario
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar usuário: {e}")
            return None  # Retorna None em caso de falha

    @staticmethod
    def usuario_delete(id_usuario):
        # Exclui um usuário do banco de dados pelo ID
        try:
            usuario = UsuarioRepository.get_by_id(id_usuario)
            if not usuario:
                raise ValueError("Usuário não encontrado.")

            db.session.delete(usuario)  # Remove o usuário
            db.session.commit()  # Confirma a transação
            return True  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar usuário: {e}")  # Log do erro
            return False  # Retorna False em caso de falha