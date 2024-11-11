from flask import Blueprint, jsonify, request
from service.cliente_service import ClienteService 
from entity.cliente import Cliente  
from exception.cliente_existente_exception import ClienteExistenteException  
from exception.cliente_email_existente_exception import ClienteEmailExistenteException

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente(id):
    # Obtém um cliente pelo ID
    try:
        cliente = ClienteService.buscar_por_id(id)
        return jsonify(cliente.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

@cliente_bp.route('', methods=['GET'])
def get_clientes():
    # Obtém todos os clientes
    clientes = ClienteService.buscar_todos()
    return jsonify(clientes)

@cliente_bp.route('', methods=['POST'])
def cadastrar_cliente():
    # Cadastra um novo cliente
    data = request.get_json()
    cliente = Cliente(
        nome=data['nome'],
        email=data['email'],
        senha=data['senha'],
        telefone=data['telefone'],
        endereco=data['endereco']
        # Adicione outros atributos necessários para o Cliente aqui
    )
    
    try:
        cliente_salvo = ClienteService.cadastrar_cliente(cliente)
        return jsonify(cliente_salvo.to_dict()), 201
    except ClienteEmailExistenteException as em:
        print(f'Caiu na Exception do email! error : {em}')
        return jsonify({"Error": str(em)}), 409
    except ClienteExistenteException as ce:
        return jsonify({"Error": str(ce)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
    


@cliente_bp.route('/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    
    #Atualiza as informações de um cliente existente.
    data = request.get_json()
    cliente = Cliente(
        id=id,  # Usar o ID fornecido na URL
        nome=data['nome'],
        email=data['email'],
        senha=data['senha'],
        telefone=data['telefone'],
        endereco=data['endereco']
        # Adicione outros atributos necessários para o Cliente aqui
    )
    
    try:
        cliente_atualizado = ClienteService.atualizar_cliente(cliente)
        return jsonify(cliente_atualizado.to_dict()), 200
    except ClienteEmailExistenteException as em:
        return jsonify({"Error": str(em)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@cliente_bp.route('/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    #Exclui um cliente pelo ID
    try:
        if ClienteService.deletar_cliente(id):
            return jsonify({"Message": "Cliente excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o cliente."}), 400
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500    
    