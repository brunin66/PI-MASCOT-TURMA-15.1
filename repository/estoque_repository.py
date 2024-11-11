from entity.estoque import Estoque
from db import db

class EstoqueRepository:

    @staticmethod
    def get_all():
        # Retorna todos os itens no estoque
        return Estoque.query.all()

    @staticmethod
    def get_by_id(id_item):
        # Retorna um item pelo ID
        return Estoque.query.get(id_item)
    
    @staticmethod
    def get_by_nome(nome):
        # Retorna um item pelo nome
        return Estoque.query.filter_by(nome=nome).first()
    
    @staticmethod
    def create(estoque):
        # Cria um novo item no estoque
        try:
            db.session.add(estoque)
            db.session.commit()
            return estoque
        except Exception as e:
            db.session.rollback()  # Reverte em caso de erro
            return None  # Retorna None em caso de falha

    @staticmethod
    def update(estoque):
        # Atualiza as informações de um item existente no estoque
        try:
            existing_estoque = EstoqueRepository.get_by_id(estoque.id_item)
            if not existing_estoque:
                raise ValueError("Item não encontrado.")
            
            # Atualiza os campos
            existing_estoque.nome = estoque.nome
            existing_estoque.descricao = estoque.descricao
            existing_estoque.quantidade = estoque.quantidade
            existing_estoque.preco = estoque.preco
            existing_estoque.tipo = estoque.tipo
            existing_estoque.validade = estoque.validade

            db.session.commit()
            return existing_estoque
        except Exception as e:
            db.session.rollback()
            return None

    @staticmethod
    def delete(id_item):
        # Exclui um item do estoque pelo ID
        try:
            estoque = EstoqueRepository.get_by_id(id_item)
            if not estoque:
                raise ValueError("Item não encontrado.")
            
            db.session.delete(estoque)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False