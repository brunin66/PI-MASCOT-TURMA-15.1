from entity.servico import Servico
from db import db

class ServicoRepository:

    @staticmethod
    def get_all():
        # Retorna todos os serviços cadastrados no banco de dados
        return Servico.query.all()

    @staticmethod
    def get_by_id(id_servico):
        # Retorna um serviço pelo ID
        return Servico.query.get(id_servico)

    @staticmethod
    def get_by_nome(nome):
        # Retorna um serviço pelo nome
        return Servico.query.filter_by(nome=nome).first()

    @staticmethod
    def create(servico):
        # Cria um novo serviço no banco de dados
        try:
            db.session.add(servico)  # Adiciona o serviço à sessão
            db.session.commit()      # Comita a transação
            return servico
        except Exception as e:
            db.session.rollback()    # Caso haja erro, faz rollback da transação
            print(f"Erro ao criar serviço: {e}")
            return None

    @staticmethod
    def update(servico):
        # Atualiza as informações de um serviço existente no banco de dados
        try:
            existing_servico = ServicoRepository.get_by_id(servico.id_servico)
            if not existing_servico:
                raise ValueError("Serviço não encontrado.")

            existing_servico.nome = servico.nome
            existing_servico.descricao = servico.descricao
            existing_servico.preco = servico.preco

            db.session.commit()
            return existing_servico
        except Exception as e:
            db.session.rollback()    # Caso haja erro, faz rollback da transação
            print(f"Erro ao atualizar serviço: {e}")
            return None

    @staticmethod
    def delete(id_servico):
        # Exclui um serviço pelo ID
        try:
            servico = ServicoRepository.get_by_id(id_servico)
            if not servico:
                raise ValueError("Serviço não encontrado.")

            db.session.delete(servico)   # Exclui o serviço
            db.session.commit()          # Comita a transação
            return True                  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()       # Caso haja erro, faz rollback da transação
            print(f"Erro ao deletar serviço: {e}")
            return False                 # Retorna False se houve erro na exclusão
