from entity.consulta import Consulta
from db import db

class ConsultaRepository:

    @staticmethod
    def get_all():
        # Retorna todas as consultas.
        return Consulta.query.all()
    
    @staticmethod
    def get_by_id(id_consulta):
        # Retorna uma consulta pelo ID
        return Consulta.query.get(id_consulta)
    
    @staticmethod
    def get_by_animal(id_animal):
        # Retorna todas as consultas de um animal específico
        return Consulta.query.filter_by(id_animal=id_animal).all()
    
    @staticmethod
    def get_by_funcionario(id_funcionario):
        # Retorna todas as consultas de um funcionário específico
        return Consulta.query.filter_by(id_funcionario=id_funcionario).all()

    @staticmethod
    def create(consulta):
        # Cria uma nova consulta no banco de dados.
        try:
            db.session.add(consulta)
            db.session.commit()
            return consulta
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao criar consulta: {e}")
            return None

    @staticmethod
    def update(consulta):
        # Atualiza uma consulta existente no banco de dados.
        try:
            existing_consulta = ConsultaRepository.get_by_id(consulta.id_consulta)
            if not existing_consulta:
                return None  # Consulta não encontrada

            # Atualiza os campos da consulta
            existing_consulta.data_consulta = consulta.data_consulta
            existing_consulta.diagnostico = consulta.diagnostico
            existing_consulta.observacoes = consulta.observacoes

            db.session.commit()  # Salva as alterações
            return existing_consulta
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar consulta: {e}")
            return None

    @staticmethod
    def delete(id_consulta):
        # Exclui uma consulta pelo ID
        try:
            consulta = ConsultaRepository.get_by_id(id_consulta)
            if not consulta:
                return False  # Consulta não encontrada

            db.session.delete(consulta)  # Remove a consulta
            db.session.commit()  # Confirma a transação
            return True  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar consulta: {e}")
            return False  # Retorna False em caso de falha
