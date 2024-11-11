from flask import Blueprint, jsonify, request
from service.medicamento_service import MedicamentoService
from exception.medicamento_existente_exception import MedicamentoExistenteException

medicamento_bp = Blueprint('medicamento', __name__)

@medicamento_bp.route('/<int:id_medicamento>', methods=['GET'])
def get_medicamento(id_medicamento):
    try:
        medicamento = MedicamentoService.buscar_por_id(id_medicamento)
        return jsonify(medicamento.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 404

@medicamento_bp.route('', methods=['GET'])
def get_medicamentos():
    # Exemplo de pegar medicamentos por item_id, ou buscar todos
    item_id = request.args.get('id_item')
    if item_id:
        medicamentos = MedicamentoService.buscar_por_item_id(item_id)
    else:
        medicamentos = MedicamentoService.buscar_todos()
    return jsonify([med.to_dict() for med in medicamentos]), 200

@medicamento_bp.route('', methods=['POST'])
def cadastrar_medicamento():
    data = request.get_json()
    medicamento = Medicamento(
        id_item=data['id_item'],
        principio_ativo=data['principio_ativo'],
        dosagem=data['dosagem'],
        fabricante=data['fabricante']
    )
    
    try:
        medicamento_salvo = MedicamentoService.cadastrar_medicamento(medicamento)
        return jsonify(medicamento_salvo.to_dict()), 201
    except MedicamentoExistenteException as e:
        return jsonify({"Error": str(e)}), 409
    except Exception as e:
        return jsonify({"Error": "Erro inesperado"}), 500

@medicamento_bp.route('/<int:id_medicamento>', methods=['PUT'])
def atualizar_medicamento(id_medicamento):
    data = request.get_json()
    medicamento = Medicamento(
        id_medicamento=id_medicamento,  # Usar o ID fornecido na URL
        id_item=data['id_item'],
        principio_ativo=data['principio_ativo'],
        dosagem=data['dosagem'],
        fabricante=data['fabricante']
    )
    
    try:
        medicamento_atualizado = MedicamentoService.atualizar_medicamento(medicamento)
        return jsonify(medicamento_atualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado"}), 500

@medicamento_bp.route('/<int:id_medicamento>', methods=['DELETE'])
def deletar_medicamento(id_medicamento):
    try:
        if MedicamentoService.deletar_medicamento(id_medicamento):
            return jsonify({"Message": "Medicamento excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o medicamento."}), 400
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado"}), 500