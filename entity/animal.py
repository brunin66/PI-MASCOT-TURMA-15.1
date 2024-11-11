from db import db  


class Animal(db.Model):
    __tablename__ = 'animal'

    # ID do animal (PK)
    id_animal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # ID do cliente (FK)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    # Nome do animal
    nome = db.Column(db.String(128), nullable=False)

    # Tipo do animal (Cachorro, Gato, etc.)
    tipo = db.Column(db.String(50), nullable=False)

    # Raça do animal
    raca = db.Column(db.String(50), nullable=False)

    # Data de nascimento do animal
    data_nascimento = db.Column(db.Date, nullable=False)

    # Sexo do animal
    sexo = db.Column(db.String(10), nullable=False)

    # Peso do animal
    peso = db.Column(db.Float, nullable=False)

    # Relacionamento com o Cliente (um cliente pode ter vários animais)
    cliente = db.relationship('Cliente', back_populates='animais')

    def to_dict(self):
        return {
            'id_animal': self.id_animal,
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'tipo': self.tipo,
            'raca': self.raca,
            'data_nascimento': str(self.data_nascimento),  
            'sexo': self.sexo,
            'peso': self.peso
        }
