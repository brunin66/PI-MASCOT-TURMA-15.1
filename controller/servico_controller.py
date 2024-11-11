from flask import Blueprint, jsonify, request
from service.servico_service import ServicoService
from exception.servico_existente_exception import ServicoExistenteException
from exception.servico_nao_encontrado_exception import ServicoNaoEncontradoException


servico_bp = Blueprint('servico', __name__)

# Rota para obter todos os serviços
@servico_bp.route('', methods=['GET'])
def get_servicos():
    try:
        servicos = ServicoService.buscar_todos()
        return jsonify(servicos), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Rota para obter um serviço pelo ID
@servico_bp.route('/<int:id_servico>', methods=['GET'])
def get_servico(id_servico):
    try:
        servico = ServicoService.buscar_por_id(id_servico)
        return jsonify(servico.to_dict()), 200
    except ServicoNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro inesperado. Tente novamente mais tarde."}), 500

# Rota para cadastrar um novo serviço
@servico_bp.route('', methods=['POST'])
def cadastrar_servico():
    data = request.get_json()
    
    servico = Servico(
        nome=data['nome'],
        descricao=data['descricao'],
        preco=data['preco']
    )
    
    try:
        servico_salvo = ServicoService.cadastrar_servico(servico)
        return jsonify(servico_salvo.to_dict()), 201
    except ServicoExistenteException as e:
        return jsonify({"Error": str(e)}), 409
    except ValorInvalidoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado. Tente novamente mais tarde."}), 500

# Rota para atualizar um serviço existente
@servico_bp.route('/<int:id_servico>', methods=['PUT'])
def atualizar_servico(id_servico):
    data = request.get_json()

    servico = Servico(
        id_servico=id_servico,
        nome=data['nome'],
        descricao=data['descricao'],
        preco=data['preco']
    )
    
    try:
        servico_atualizado = ServicoService.atualizar_servico(servico)
        return jsonify(servico_atualizado.to_dict()), 200
    except ServicoNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except ValorInvalidoException as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado. Tente novamente mais tarde."}), 500

# Rota para deletar um serviço pelo ID
@servico_bp.route('/<int:id_servico>', methods=['DELETE'])
def deletar_servico(id_servico):
    try:
        sucesso = ServicoService.deletar_servico(id_servico)
        if sucesso:
            return jsonify({"Message": "Serviço excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o serviço."}), 400
    except ServicoNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro inesperado. Tente novamente mais tarde."}), 500
