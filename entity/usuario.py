from db import db


class Usuario(db.Model):
    __tablename__ = "usuario"
    # ID
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Chave estrangeira para Funcionario
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    # Login
    login = db.Column(db.String(50), unique=True, nullable=False)
    # Senha
    senha = db.Column(db.String(255), nullable=False)
    # Perfil (Ex: admin, usuario, etc.)
    perfil = db.Column(db.String(50), nullable=False)

    # Relacionamento com a tabela Funcionario
    funcionario = db.relationship('Funcionario', backref=db.backref('usuario', uselist=False))

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'id_funcionario': self.id_funcionario,
            'login': self.login,
            'perfil': self.perfil,
            'funcionario': self.funcionario.to_dict()  # Retorna os dados do funcionário associado
        }