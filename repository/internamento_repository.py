from entity.internamento import Internamento
from db import db

class InternamentoRepository:

    @staticmethod
    def get_all():
        """Retorna todos os internamentos."""
        return Internamento.query.all()

    @staticmethod
    def get_by_id(id_internamento):
        """Retorna um internamento pelo ID."""
        return Internamento.query.get(id_internamento)

    @staticmethod
    def get_by_animal(id_animal):
        """Retorna todos os internamentos de um animal específico."""
        return Internamento.query.filter_by(id_animal=id_animal).all()

    @staticmethod
    def get_by_funcionario(id_funcionario):
        """Retorna todos os internamentos realizados por um funcionário específico."""
        return Internamento.query.filter_by(id_funcionario=id_funcionario).all()

    @staticmethod
    def create(internamento):
        """Cria um novo internamento."""
        try:
            db.session.add(internamento)
            db.session.commit()
            return internamento
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao criar internamento: {e}")
            return None

    @staticmethod
    def update(internamento):
        """Atualiza as informações de um internamento existente."""
        try:
            existing_internamento = InternamentoRepository.get_by_id(internamento.id_internamento)
            if not existing_internamento:
                raise ValueError("Internamento não encontrado.")

            existing_internamento.motivo_internamento = internamento.motivo_internamento
            existing_internamento.status = internamento.status
            existing_internamento.data_saida = internamento.data_saida

            db.session.commit()
            return existing_internamento
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar internamento: {e}")
            return None

    @staticmethod
    def delete(id_internamento):
        """Exclui um internamento pelo ID."""
        try:
            internamento = InternamentoRepository.get_by_id(id_internamento)
            if not internamento:
                raise ValueError("Internamento não encontrado.")

            db.session.delete(internamento)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao excluir internamento: {e}")
            return False
