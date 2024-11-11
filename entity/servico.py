from db import db

class Servico(db.Model):
    __tablename__ = 'servico'
    
    # ID do serviço - chave primária
    id_servico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Nome do serviço
    nome = db.Column(db.String(100), nullable=False)
    
    # Descrição do serviço
    descricao = db.Column(db.String(255), nullable=False)
    
    # Preço do serviço
    preco = db.Column(db.Float, nullable=False)
    
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    
    def to_dict(self):
        return {
            'id_servico': self.id_servico,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco
        }
