from repository.material_repository import MaterialRepository
from exception.material_existente_exception import MaterialExistenteException
from exception.material_estoque_exception import MaterialEstoqueException

class MaterialService:

    @staticmethod
    def buscar_por_id(id_material):
        # Busca um material pelo ID. Lança um erro se o material não existir.
        material = MaterialRepository.get_by_id(id_material)
        if not material:
            raise ValueError("Material não encontrado")
        return material

    @staticmethod
    def buscar_por_item(id_item):
        # Busca todos os materiais associados a um item de estoque (id_item)
        materiais = MaterialRepository.get_by_item_id(id_item)
        if not materiais:
            raise ValueError("Nenhum material encontrado para este item de estoque")
        return [material.to_dict() for material in materiais]

    @staticmethod
    def verificar_quantidade_em_estoque(id_item):
        # Verifica se há quantidade suficiente de material em estoque.
        materiais = MaterialRepository.get_by_item_id(id_item)
        if not materiais:
            raise MaterialEstoqueException("Não há materiais associados a esse item no estoque.")
        
        quantidade_total = sum([material.quantidade_em_estoque for material in materiais])
        return quantidade_total

    @staticmethod
    def cadastrar_material(material):
        # Cadastra um novo material no banco de dados, validando o tipo e a quantidade.
        if len(material.tipo_material) < 3:
            raise ValueError("Tipo de material precisa ter pelo menos 3 caracteres")

        # Verificar se o material já existe no estoque pelo ID do item
        materiais_existentes = MaterialRepository.get_by_item_id(material.id_item)
        for mat in materiais_existentes:
            if mat.tipo_material == material.tipo_material:
                raise MaterialExistenteException("Material deste tipo já está cadastrado para este item de estoque.")

        # Se todas as validações passarem, cria o novo material
        return MaterialRepository.create(material)

    @staticmethod
    def atualizar_material(material):
        # Atualiza as informações de um material existente no banco de dados
        if len(material.tipo_material) < 3:
            raise ValueError("Tipo de material precisa ter pelo menos 3 caracteres")
        
        # Verifica se o material já existe antes de atualizar
        existing_material = MaterialRepository.get_by_id(material.id_material)
        if not existing_material:
            raise ValueError("Material não encontrado")

        return MaterialRepository.update(material)

    @staticmethod
    def deletar_material(id_material):
        # Exclui um material do banco de dados pelo ID
        if MaterialRepository.delete(id_material):
            return {"Message": "Material excluído com sucesso."}
        else:
            raise ValueError("Falha ao excluir o material.")