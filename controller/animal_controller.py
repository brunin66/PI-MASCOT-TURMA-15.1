from flask import Blueprint, jsonify, request
from service.animal_service import AnimalService
from entity.animal import Animal
from exception.animal_existente_exception import AnimalExistenteException
from exception.animal_nao_encontrado_exception import AnimalNaoEncontradoException

# Criando o blueprint para as rotas de animais
animal_bp = Blueprint('animal', __name__)

@animal_bp.route('/<int:id_animal>', methods=['GET'])
def get_animal(id_animal):
    # Rota para obter um animal pelo ID
    try:
        animal = AnimalService.buscar_por_id(id_animal)
        return jsonify(animal.to_dict()), 200
    except AnimalNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@animal_bp.route('', methods=['GET'])
def get_animais():
    # Rota para obter todos os animais
    try:
        animais = AnimalService.buscar_todos()
        return jsonify(animais), 200
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@animal_bp.route('/cliente/<int:id_cliente>', methods=['GET'])
def get_animais_por_cliente(id_cliente):
    # Rota para obter todos os animais de um cliente específico
    try:
        animais = AnimalService.buscar_por_cliente(id_cliente)
        return jsonify(animais), 200
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@animal_bp.route('', methods=['POST'])
def cadastrar_animal():
    # Rota para cadastrar um novo animal
    data = request.get_json()
    try:
        # Criando a instância de Animal a partir dos dados recebidos
        animal = Animal(
            nome=data['nome'],
            id_cliente=data['id_cliente'],
            tipo=data['tipo'],
            raca=data['raca'],
            data_nascimento=data['data_nascimento'],
            sexo=data['sexo'],
            peso=data['peso']
        )
        # Chamando o service para cadastrar o animal
        animal_salvo = AnimalService.cadastrar_animal(animal)
        return jsonify(animal_salvo.to_dict()), 201
    except AnimalExistenteException as e:
        return jsonify({"Error": str(e)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@animal_bp.route('/<int:id_animal>', methods=['PUT'])
def atualizar_animal(id_animal):
    # Rota para atualizar um animal existente
    data = request.get_json()
    try:
        animal = Animal(
            id_animal=id_animal,  # ID fornecido na URL
            nome=data['nome'],
            id_cliente=data['id_cliente'],
            tipo=data['tipo'],
            raca=data['raca'],
            data_nascimento=data['data_nascimento'],
            sexo=data['sexo'],
            peso=data['peso']
        )
        # Chamando o service para atualizar o animal
        animal_atualizado = AnimalService.atualizar_animal(animal)
        return jsonify(animal_atualizado.to_dict()), 200
    except AnimalNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@animal_bp.route('/<int:id_animal>', methods=['DELETE'])
def deletar_animal(id_animal):
    # Rota para deletar um animal pelo ID
    try:
        resultado = AnimalService.deletar_animal(id_animal)
        return jsonify(resultado), 204
    except AnimalNaoEncontradoException as e:
        return jsonify({"Error": str(e)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500
