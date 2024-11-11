from db import db
from datetime import datetime

class Estoque(db.Model):
    __tablename__ = "estoque"
    
    # ID do item (Primary Key)
    id_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Nome do item
    nome = db.Column(db.String(128), nullable=False)
    
    # Descrição do item
    descricao = db.Column(db.String(255), nullable=True)
    
    # Quantidade em estoque
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    
    # Preço do item
    preco = db.Column(db.Float, nullable=False)
    
    # Tipo do item (Medicamento, Material, etc.)
    tipo = db.Column(db.String(50), nullable=False)
    
    # Validade (apenas para medicamentos)
    validade = db.Column(db.Date, nullable=True)
    
    def __init__(self, nome, descricao, quantidade, preco, tipo, validade=None):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo
        self.validade = validade
