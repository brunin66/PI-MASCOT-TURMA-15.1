from db import db

class Consulta(db.Model):
    __tablename__ = 'consulta'
    
    # ID da consulta (PK)
    id_consulta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # ID do animal (FK)
    id_animal = db.Column(db.Integer, db.ForeignKey('animal.id_animal'), nullable=False)
    
    # ID do funcionário (FK)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    
    # Data da consulta
    data_consulta = db.Column(db.DateTime, nullable=False)
    
    # Diagnóstico da consulta
    diagnostico = db.Column(db.String(255), nullable=True)
    
    # Observações
    observacoes = db.Column(db.Text, nullable=True)
    
    # Relacionamento com a tabela Animal
    animal = db.relationship('Animal', backref='consultas', lazy=True)
    
    # Relacionamento com a tabela Funcionario
    funcionario = db.relationship('Funcionario', backref='consultas', lazy=True)

    def __init__(self, id_animal, id_funcionario, data_consulta, diagnostico=None, observacoes=None):
        self.id_animal = id_animal
        self.id_funcionario = id_funcionario
        self.data_consulta = data_consulta
        self.diagnostico = diagnostico
        self.observacoes = observacoes

    def to_dict(self):
        return {
            'id_consulta': self.id_consulta,
            'id_animal': self.id_animal,
            'id_funcionario': self.id_funcionario,
            'data_consulta': self.data_consulta.strftime('%Y-%m-%d %H:%M:%S'),
            'diagnostico': self.diagnostico,
            'observacoes': self.observacoes
        }
