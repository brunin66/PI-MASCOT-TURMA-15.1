from repository.estoque_repository import EstoqueRepository
from entity.estoque import Estoque
from exception.item_existente_exception import ItemExistenteException

class EstoqueService:

    @staticmethod
    def buscar_por_id(id_item):
        # Busca um item no estoque pelo ID
        estoque = EstoqueRepository.get_by_id(id_item)
        if not estoque:
            raise ValueError("Item não encontrado")
        return estoque

    @staticmethod
    def buscar_todos():
        # Retorna todos os itens do estoque
        estoque = EstoqueRepository.get_all()
        return [item.to_dict() for item in estoque]

    @staticmethod
    def cadastrar_item(estoque):
        # Valida e cadastra um novo item no estoque
        if EstoqueService.verificar_item_existente(estoque.nome):
            raise EstoqueExistenteException("Item já existe no estoque")
        
        return EstoqueRepository.create(estoque)

    @staticmethod
    def atualizar_item(estoque):
        # Atualiza um item no estoque
        return EstoqueRepository.update(estoque)

    @staticmethod
    def deletar_item(id_item):
        # Exclui um item do estoque
        return EstoqueRepository.delete(id_item)

    @staticmethod
    def verificar_item_existente(nome):
        # Verifica se um item com o mesmo nome já existe
        return EstoqueRepository.get_by_nome(nome) is not None