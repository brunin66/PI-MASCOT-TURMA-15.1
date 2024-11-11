from db import db

class Material(db.Model):
    __tablename__ = 'material'
    
    # ID do Material (PK)
    id_material = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # ID do Item (FK para a tabela Estoque)
    id_item = db.Column(db.Integer, db.ForeignKey('estoque.id_item'), nullable=False)
    
    # Relacionamento com a tabela Estoque (para acessar o item do estoque relacionado)
    item = db.relationship('Estoque', backref='materiais', lazy=True)
    
    # Tipo do Material (Ex: Medicamento, Material de escritório, etc.)
    tipo_material = db.Column(db.String(100), nullable=False)
    
    # Quantidade disponível em estoque
    quantidade_em_estoque = db.Column(db.Integer, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'id_material': self.id_material,
            'id_item': self.id_item,
            'tipo_material': self.tipo_material,
            'quantidade_em_estoque': self.quantidade_em_estoque,
            'item': self.item.to_dict() if self.item else None
        }