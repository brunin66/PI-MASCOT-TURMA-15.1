from db import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    # ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Nome
    nome = db.Column(db.String(128), nullable=False)
    # Email
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Telefone
    telefone = db.Column(db.String(15), nullable=False)
    # Endereço
    endereco = db.Column(db.String(100), nullable=False)

    animais = db.relationship('Animal', back_populates='cliente', cascade='all, delete-orphan')
    

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco
        }
    
    def to_dict_resumida(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
