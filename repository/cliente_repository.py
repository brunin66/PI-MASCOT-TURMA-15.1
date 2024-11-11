from entity.cliente import Cliente  # Importando o modelo Cliente
from db import db

class ClienteRepository:

    @staticmethod
    def get_all():
        # Retorna todos os clientes.
        return Cliente.query.all()
    
    @staticmethod
    def get_by_id(id):
        # Retorna um cliente pelo ID
        return Cliente.query.get(id)
    
    @staticmethod
    def get_by_nome(nome):
        # Retorna um cliente pelo nome
        return Cliente.query.filter_by(nome=nome).first()
    
    @staticmethod
    def get_by_email(email):
        # Retorna todos os clientes com o email especificado
        return Cliente.query.filter_by(email=email).all()

    @staticmethod
    def create_cliente(cliente):
        # Cria um novo cliente no banco de dados.
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            return None  # Retorna None em caso de falha
        
    @staticmethod
    def cliente_update(cliente):
        #Atualiza as informações de um cliente existente no banco de dados.
        try:
            cliente_existente = ClienteRepository.get_by_id(cliente.id)
            if not cliente_existente:
                raise ValueError("Cliente não encontrado.")

            # Atualiza os campos do cliente
            cliente_existente.nome = cliente.nome
            cliente_existente.email = cliente.email
            # Adicione outros campos que precisam ser atualizados aqui

            db.session.commit()  # Salva as alterações
            return cliente_existente
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar cliente: {e}")  # Log do erro
            return None  # Retorna None em caso de falha
        

    @staticmethod
    def delete(id):
        #Exclui um cliente do banco de dados pelo ID
        try:
            cliente = ClienteRepository.get_by_id(id)
            if not cliente:
                raise ValueError("Cliente não encontrado.")

            db.session.delete(cliente)  # Remove o cliente
            db.session.commit()  # Confirma a transação
            return True  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar cliente: {e}")  # Log do erro
            return False  # Retorna False em caso de falha