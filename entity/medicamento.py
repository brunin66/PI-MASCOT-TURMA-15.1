from db import db

class Medicamento(db.Model):
    __tablename__ = "medicamento"
    
    id_medicamento = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_item = db.Column(db.Integer, db.ForeignKey('estoque.id_item'), nullable=False)
    
    # Relacionamento com a tabela Estoque (para acessar o item do estoque relacionado)
    item = db.relationship('Estoque', backref='medicamentos', lazy=True)
    
    principio_ativo = db.Column(db.String(255), nullable=False)
    
    dosagem = db.Column(db.String(255), nullable=False)
    
    fabricante = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            'id_medicamento': self.id_medicamento,
            'id_item': self.id_item,
            'principio_ativo': self.principio_ativo,
            'dosagem': self.dosagem,
            'fabricante': self.fabricante,
            'item': self.item.to_dict() if self.item else None
        }