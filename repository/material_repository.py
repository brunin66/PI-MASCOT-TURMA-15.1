from entity.material import Material
from db import db

class MaterialRepository:

    @staticmethod
    def get_all():
        # Retorna todos os materiais
        return Material.query.all()

    @staticmethod
    def get_by_id(id_material):
        # Retorna um material pelo ID
        return Material.query.get(id_material)

    @staticmethod
    def get_by_item_id(id_item):
        # Retorna os materiais pelo ID do item (estoque)
        return Material.query.filter_by(id_item=id_item).all()

    @staticmethod
    def create(material):
        # Cria um novo material no banco de dados
        try:
            db.session.add(material)
            db.session.commit()
            return material
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao criar material: {e}")
            return None

    @staticmethod
    def update(material):
        # Atualiza um material no banco de dados
        try:
            existing_material = MaterialRepository.get_by_id(material.id_material)
            if not existing_material:
                raise ValueError("Material não encontrado.")
            
            # Atualiza os campos do material
            existing_material.tipo_material = material.tipo_material
            existing_material.quantidade_em_estoque = material.quantidade_em_estoque
            db.session.commit()  # Salva as alterações
            return existing_material
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao atualizar material: {e}")
            return None

    @staticmethod
    def delete(id_material):
        # Exclui um material pelo ID
        try:
            material = MaterialRepository.get_by_id(id_material)
            if not material:
                raise ValueError("Material não encontrado.")
            
            db.session.delete(material)  # Remove o material
            db.session.commit()  # Confirma a transação
            return True
        except Exception as e:
            db.session.rollback()  # Reverte a sessão em caso de erro
            print(f"Erro ao deletar material: {e}")
            return False