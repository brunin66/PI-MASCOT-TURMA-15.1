from db import db
from datetime import datetime

class Internamento(db.Model):
    __tablename__ = 'internamento'
    
    # ID do Internamento (PK)
    id_internamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Referência ao Animal (FK)
    id_animal = db.Column(db.Integer, db.ForeignKey('animal.id_animal'), nullable=False)
    
    # Referência ao Funcionario (FK)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    
    # Data de Internamento
    data_internamento = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Data de Saída
    data_saida = db.Column(db.DateTime, nullable=True)
    
    # Motivo do Internamento
    motivo_internamento = db.Column(db.String(255), nullable=False)
    
    # Status do Internamento (Ativo, Finalizado, etc.)
    status = db.Column(db.String(20), nullable=False, default='Ativo')  # 'Ativo', 'Finalizado', etc.

    # Relacionamentos
    animal = db.relationship('Animal', backref=db.backref('internamentos', lazy=True))
    funcionario = db.relationship('Funcionario', backref=db.backref('internamentos', lazy=True))

    def __init__(self, id_animal, id_funcionario, motivo_internamento, status='Ativo', data_saida=None):
        self.id_animal = id_animal
        self.id_funcionario = id_funcionario
        self.motivo_internamento = motivo_internamento
        self.status = status
        self.data_saida = data_saida

    def to_dict(self):
        return {
            'id_internamento': self.id_internamento,
            'id_animal': self.id_animal,
            'id_funcionario': self.id_funcionario,
            'data_internamento': self.data_internamento.strftime('%Y-%m-%d %H:%M:%S'),
            'data_saida': self.data_saida.strftime('%Y-%m-%d %H:%M:%S') if self.data_saida else None,
            'motivo_internamento': self.motivo_internamento,
            'status': self.status
        }

