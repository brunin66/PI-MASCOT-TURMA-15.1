from flask import Blueprint, jsonify, request
from service.estoque_service import EstoqueService
from entity.estoque import Estoque
from exception.item_existente_exception import ItemExistenteException

estoque_bp = Blueprint('estoque', __name__)

@estoque_bp.route('/<int:id_item>', methods=['GET'])
def get_item(id_item):
    # Obtém um item do estoque pelo ID
    try:
        item = EstoqueService.buscar_por_id(id_item)
        return jsonify(item.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

@estoque_bp.route('', methods=['GET'])
def get_estoque():
    # Obtém todos os itens do estoque
    try:
        estoque = EstoqueService.buscar_todos()
        return jsonify(estoque), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@estoque_bp.route('', methods=['POST'])
def cadastrar_item():
    # Cadastra um novo item no estoque
    data = request.get_json()
    
     # Validações
    if not data.get('nome'):
        return jsonify({"Error": "O nome do item é obrigatório"}), 400
    
    if data['quantidade'] < 0:
        return jsonify({"Error": "A quantidade não pode ser negativa"}), 400
    
    if data['preco'] <= 0:
        return jsonify({"Error": "O preço deve ser maior que zero"}), 400
    
    if data['tipo'] not in ['Medicamento', 'Material', 'Outro']:  # Exemplo de tipos permitidos
        return jsonify({"Error": "Tipo inválido"}), 400
    
    if data['tipo'] == 'Medicamento' and not data.get('validade'):
        return jsonify({"Error": "A validade é obrigatória para medicamentos"}), 400

    
    # Criação do objeto Estoque com os dados recebidos
    item = Estoque(
        nome=data['nome'],
        descricao=data.get('descricao', ''),
        quantidade=data['quantidade'],
        preco=data['preco'],
        tipo=data['tipo'],
        validade=data.get('validade')  # 'validade' pode ser None, caso não seja um medicamento
    )
    
    try:
        item_salvo = EstoqueService.cadastrar_item(item)
        return jsonify(item_salvo.to_dict()), 201
    except EstoqueExistenteException as e:
        return jsonify({"Error": str(e)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500