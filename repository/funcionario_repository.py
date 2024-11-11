from entity.funcionario import Funcionario  # Importando o modelo Funcionario
from db import db

class FuncionarioRepository:

    @staticmethod
    def get_all():
        #Retorna todos os funcionários.
        return Funcionario.query.all()
    
    @staticmethod
    def get_by_id(id):
        #Retorna um funcionário pelo ID
        return Funcionario.query.get(id)
    
    @staticmethod
    def get_by_nome(nome):
        #Retorna um funcionário pelo nome
        return Funcionario.query.filter_by(nome=nome).first()
    

    @staticmethod
    def get_by_email(email):
        return Funcionario.query.filter_by(email=email).all()

    @staticmethod
    def create(funcionario):
        #Cria um novo funcionário no banco de dados.
        try:
            # consultar se existe funcionario com o email
            # caso sim retorna Erro EmailExistenteException
        

            db.session.add(funcionario)
            db.session.commit()
            return funcionario
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            return None  # Retorna None em caso de falha
    @staticmethod
    def funcionario_update(funcionario):
        #Atualiza as informações de um funcionário existente no banco de dados.
        try:
            existing_funcionario = FuncionarioRepository.get_by_id(funcionario.id)
            if not existing_funcionario:
                raise ValueError("Funcionário não encontrado.")

            # Atualiza os campos do funcionário
            existing_funcionario.nome = funcionario.nome
            existing_funcionario.email = funcionario.email
            # Adicione outros campos que precisam ser atualizados aqui

            db.session.commit()  # Salva as alterações
            return existing_funcionario
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar funcionário: {e}")  # Log do erro
            return None  # Retorna None em caso de falha

    @staticmethod
    def funcionario_delete(id):
        #Exclui um funcionário do banco de dados pelo ID
        try:
            funcionario = FuncionarioRepository.get_by_id(id)
            if not funcionario:
                raise ValueError("Funcionário não encontrado.")

            db.session.delete(funcionario)  # Remove o funcionário
            db.session.commit()  # Confirma a transação
            return True  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar funcionário: {e}")  # Log do erro
            return False  # Retorna False em caso de falha       