from repository.medicamento_repository import MedicamentoRepository
from entity.medicamento import Medicamento
from exception.medicamento_existente_exception import MedicamentoExistenteException

class MedicamentoService:

    @staticmethod
    def buscar_por_id(id_medicamento):
        # Busca um medicamento pelo ID
        medicamento = MedicamentoRepository.get_by_id(id_medicamento)
        if not medicamento:
            raise ValueError("Medicamento não encontrado")
        return medicamento
    
    @staticmethod
    def buscar_por_item_id(id_item):
        # Busca medicamentos associados a um item no estoque
        return MedicamentoRepository.get_by_item_id(id_item)
    
    @staticmethod
    def cadastrar_medicamento(medicamento):
        # Cadastra um novo medicamento
        return MedicamentoRepository.create(medicamento)
    
    @staticmethod
    def atualizar_medicamento(medicamento):
        # Atualiza as informações de um medicamento existente
        return MedicamentoRepository.update(medicamento)
    
    @staticmethod
    def deletar_medicamento(id_medicamento):
        # Deleta um medicamento pelo ID
        return MedicamentoRepository.delete(id_medicamento)