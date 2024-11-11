from flask import Blueprint, jsonify, request
from service.funcionario_service import FuncionarioService  
from entity.funcionario import Funcionario  
from exception.funcionario_existente_exception import FuncionarioExistenteException  
from exception.funcionario_email_existente_exception import FuncionarioEmailExistenteException

funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/<int:id>', methods=['GET'])
def get_funcionario(id):
    #Obtém um funcionário pelo ID
    try:
        funcionario = FuncionarioService.buscar_por_id(id)
        return jsonify(funcionario.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

@funcionario_bp.route('', methods=['GET'])
def get_funcionarios():
    #Obtém todos os funcionários.
    funcionarios = FuncionarioService.buscar_todos()
    return jsonify(funcionarios)

@funcionario_bp.route('', methods=['POST'])
def cadastrar_funcionario():
    #Cadastra um novo funcionário.
    data = request.get_json()
    funcionario = Funcionario(
        nome=data['nome'],
        cargo=data['cargo'],
        email=data['email'],
        senha=data['senha'],
        crm=data['crm'],
        cpf=data['cpf']
        

    )
    
    try:
        funcionario_salvo = FuncionarioService.cadastrar_funcionario(funcionario)
        return jsonify(funcionario_salvo.to_dict()), 201
    except FuncionarioEmailExistenteException as em:
        return jsonify ({"Error": str(em)}), 409
    except FuncionarioExistenteException as fee:
        return jsonify({"Error": str(fee)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
    

@funcionario_bp.route('/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    #Atualiza as informações de um funcionário existente
    data = request.get_json()
    funcionario = Funcionario(
        id=id,  # Usar o ID fornecido na URL
        nome=data['nome'],
        cargo=data['cargo'],
        email=data['email'],
        senha=data['senha'],
        crm=data['crm'],
        cpf=data['cpf']
    )
    
    try:
        funcionario_atualizado = FuncionarioService.atualizar_funcionario(funcionario)
        return jsonify(funcionario_atualizado.to_dict()), 200
    except FuncionarioEmailExistenteException as em:
        return jsonify({"Error": str(em)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        print(f'Caiu na Exception Generica, error: {ex}')
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@funcionario_bp.route('/<int:id>', methods=['DELETE'])
def deletar_funcionario(id):
    #Exclui um funcionário pelo ID."""
    try:
        if FuncionarioService.deletar_funcionario(id):
            return jsonify({"Message": "Funcionário excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o funcionário."}), 400
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
