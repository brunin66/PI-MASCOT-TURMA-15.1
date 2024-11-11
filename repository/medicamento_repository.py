from entity.medicamento import Medicamento
from db import db

class MedicamentoRepository:

    @staticmethod
    def get_all():
        # Retorna todos os medicamentos
        return Medicamento.query.all()
    
    @staticmethod
    def get_by_id(id_medicamento):
        # Retorna um medicamento pelo ID
        return Medicamento.query.get(id_medicamento)
    
    @staticmethod
    def get_by_item_id(id_item):
        # Retorna os medicamentos pelo ID do item (estoque)
        return Medicamento.query.filter_by(id_item=id_item).all()

    @staticmethod
    def create(medicamento):
        # Cria um novo medicamento no banco de dados
        try:
            db.session.add(medicamento)
            db.session.commit()
            return medicamento
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao criar medicamento: {e}")
            return None
    
    @staticmethod
    def update(medicamento):
        # Atualiza um medicamento no banco de dados
        try:
            existing_medicamento = MedicamentoRepository.get_by_id(medicamento.id_medicamento)
            if not existing_medicamento:
                raise ValueError("Medicamento não encontrado.")
            
            # Atualiza os campos do medicamento
            existing_medicamento.principio_ativo = medicamento.principio_ativo
            existing_medicamento.dosagem = medicamento.dosagem
            existing_medicamento.fabricante = medicamento.fabricante
            # Atualize qualquer outro campo necessário aqui

            db.session.commit()  # Salva as alterações
            return existing_medicamento
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar medicamento: {e}")
            return None
    
    @staticmethod
    def delete(id_medicamento):
        # Exclui um medicamento pelo ID
        try:
            medicamento = MedicamentoRepository.get_by_id(id_medicamento)
            if not medicamento:
                raise ValueError("Medicamento não encontrado.")
            
            db.session.delete(medicamento)  # Remove o medicamento
            db.session.commit()  # Confirma a transação
            return True  # Retorna True se a exclusão for bem-sucedida
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar medicamento: {e}")
            return False  # Retorna False em caso de falha