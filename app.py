from flask import Flask
from config import Config
from db import db
from init_db import init_db
from controller.funcionario_controller import funcionario_bp
from controller.cliente_controller import cliente_bp
from controller.usuario_controller import usuario_bp
from controller.estoque_controller import estoque_bp
from controller.medicamento_controller import medicamento_bp
from controller.material_controller import material_bp
from controller.animal_controller import animal_bp
from controller.servico_controller import servico_bp
from controller.consulta_controller import consulta_bp
from controller.internamento_controller import internamento_bp




app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

init_db(app)

app.register_blueprint(funcionario_bp, url_prefix='/api/funcionarios')
app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
app.register_blueprint(estoque_bp, url_prefix='/api/estoque')
app.register_blueprint(medicamento_bp, url_prefix='/api/medicamento')
app.register_blueprint(material_bp, url_prefix='/api/material')
app.register_blueprint(animal_bp, url_prefix='/api/animal')
app.register_blueprint(servico_bp, url_prefix='/api/servico')
app.register_blueprint(consulta_bp, url_prefix='/api/consulta')
app.register_blueprint(internamento_bp, url_prefix='/api/internamento')








if __name__ == "__main__":
    app.run(debug=True)