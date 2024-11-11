from flask import Blueprint, jsonify, request
from service.internamento_service import InternamentoService
from exception.internamento_exception import InternamentoException
from flask_jwt_extended import jwt_required

internamento_bp = Blueprint('internamento', __name__)

# Rota para buscar um internamento pelo ID
@internamento_bp.route('/<int:id>', methods=['GET'])
@jwt_required()  # Exige autenticação via JWT
def get_internamento(id):
    """Buscar um internamento pelo ID"""
    try:
        internamento = InternamentoService.buscar_por_id(id)
        return jsonify(internamento.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except InternamentoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

# Rota para buscar todos os internamentos (com paginação)
@internamento_bp.route('', methods=['GET'])
@jwt_required()  # Exige autenticação via JWT
def get_internamentos():
    """Buscar todos os internamentos com paginação"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        internamentos = InternamentoService.buscar_todos_paginados(page, per_page)
        return jsonify(internamentos), 200
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

# Rota para cadastrar um novo internamento
@internamento_bp.route('', methods=['POST'])
@jwt_required()  # Exige autenticação via JWT
def cadastrar_internamento():
    """Cadastrar um novo internamento"""
    data = request.get_json()

    # Verificação básica para os dados obrigatórios
    if not all(k in data for k in ('id_animal', 'id_funcionario', 'data_internamento', 'motivo_internamento', 'status')):
        return jsonify({"Error": "Faltam dados obrigatórios."}), 400

    try:
        # Criar o objeto Internamento com os dados fornecidos
        internamento = Internamento(
            id_animal=data['id_animal'],
            id_funcionario=data['id_funcionario'],
            data_internamento=data['data_internamento'],
            motivo_internamento=data['motivo_internamento'],
            status=data['status']
        )

        # Chamar o service para salvar o internamento
        internamento_salvo = InternamentoService.cadastrar_internamento(internamento)
        return jsonify(internamento_salvo.to_dict()), 201
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except InternamentoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

# Rota para atualizar um internamento existente
@internamento_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()  # Exige autenticação via JWT
def atualizar_internamento(id):
    """Atualizar um internamento existente"""
    data = request.get_json()

    # Verificação básica para os dados obrigatórios
    if not all(k in data for k in ('id_animal', 'id_funcionario', 'data_internamento', 'motivo_internamento', 'status')):
        return jsonify({"Error": "Faltam dados obrigatórios."}), 400

    try:
        # Criar o objeto Internamento com os dados fornecidos
        internamento = Internamento(
            id=id,  # Usando o ID fornecido na URL
            id_animal=data['id_animal'],
            id_funcionario=data['id_funcionario'],
            data_internamento=data['data_internamento'],
            motivo_internamento=data['motivo_internamento'],
            status=data['status']
        )

        # Chamar o service para atualizar o internamento
        internamento_atualizado = InternamentoService.atualizar_internamento(internamento)
        return jsonify(internamento_atualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except InternamentoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

# Rota para excluir um internamento
@internamento_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # Exige autenticação via JWT
def deletar_internamento(id):
    """Excluir um internamento pelo ID"""
    try:
        if InternamentoService.deletar_internamento(id):
            return jsonify({"Message": "Internamento excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o internamento."}), 400
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except InternamentoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
