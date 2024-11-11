from db import db


class Funcionario(db.Model):
    __tablename__ = "funcionario"
    #ID
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    #Nome
    nome = db.Column(db.String(128), nullable = False)
    #email
    email = db.Column(db.String(100), unique = True, nullable = False)
    #Senha
    senha = db.Column(db.String(40), nullable = False)
    #CPF
    cpf = db.Column(db.String(14))
    #Cargo
    cargo = db.Column(db.String(30), nullable = False)
    #CRM obrigatório apenas para veterinários
    crm = db.Column(db.String(10), nullable = True)



    def to_dict(self):
        return {'id':self.id,
                'nome':self.nome,
                'email':self.email,
                'cpf':self.cpf,
                'cargo':self.cargo,
                'crm':self.crm
        }