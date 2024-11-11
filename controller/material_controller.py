from flask import Blueprint, jsonify, request
from service.material_service import MaterialService
from entity.material import Material
from exception.material_existente_exception import MaterialExistenteException
from exception.material_estoque_exception import MaterialEstoqueException

material_bp = Blueprint('material', __name__)

# Rota para buscar um material pelo ID
@material_bp.route('/<int:id_material>', methods=['GET'])
def get_material(id_material):
    try:
        material = MaterialService.buscar_por_id(id_material)
        return jsonify(material.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500


# Rota para buscar materiais de um item específico
@material_bp.route('/item/<int:id_item>', methods=['GET'])
def get_materials_by_item(id_item):
    try:
        materiais = MaterialService.buscar_por_item(id_item)
        return jsonify(materiais), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500


# Rota para cadastrar um novo material
@material_bp.route('', methods=['POST'])
def create_material():
    data = request.get_json()
    material = Material(
        id_item=data['id_item'],
        tipo_material=data['tipo_material'],
        quantidade_em_estoque=data['quantidade_em_estoque']
    )
    try:
        material_salvo = MaterialService.cadastrar_material(material)
        return jsonify(material_salvo.to_dict()), 201
    except MaterialExistenteException as e:
        return jsonify({"Error": str(e)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500


# Rota para atualizar um material
@material_bp.route('/<int:id_material>', methods=['PUT'])
def update_material(id_material):
    data = request.get_json()
    material = Material(
        id_material=id_material,
        id_item=data['id_item'],
        tipo_material=data['tipo_material'],
        quantidade_em_estoque=data['quantidade_em_estoque']
    )
    try:
        material_atualizado = MaterialService.atualizar_material(material)
        return jsonify(material_atualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500


# Rota para excluir um material
@material_bp.route('/<int:id_material>', methods=['DELETE'])
def delete_material(id_material):
    try:
        result = MaterialService.deletar_material(id_material)
        return jsonify(result), 204
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
