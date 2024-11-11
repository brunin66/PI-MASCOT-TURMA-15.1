from flask import Blueprint, jsonify, request
from service.consulta_service import ConsultaService
from datetime import datetime
from exception.consulta_existente_exception import ConsultaExistenteException
from exception.consulta_nao_encontrada_exception import ConsultaNaoEncontradaException

consulta_bp = Blueprint('consulta', __name__)

def validar_data_consulta(data_consulta_str):
    try:
        return datetime.strptime(data_consulta_str, '%Y-%m-%d %H:%M:%S')  # Formato de data
    except ValueError:
        raise ValueError("Formato de data inválido. Use o formato 'YYYY-MM-DD HH:MM:SS'.")

def formatar_resposta_erro(mensagem, status_code):
    return jsonify({"error": mensagem}), status_code

@consulta_bp.route('/<int:id_consulta>', methods=['GET'])
def get_consulta(id_consulta):
    try:
        consulta = ConsultaService.buscar_por_id(id_consulta)
        return jsonify(consulta.to_dict()), 200
    except ConsultaNaoEncontradaException as e:
        return formatar_resposta_erro(str(e), 404)
    except Exception as e:
        return formatar_resposta_erro("Erro inesperado. Tente novamente mais tarde.", 500)


@consulta_bp.route('', methods=['GET'])
def get_consultas():
    try:
        consultas = ConsultaService.buscar_todas()
        return jsonify(consultas), 200
    except Exception as e:
        return formatar_resposta_erro("Erro inesperado. Tente novamente mais tarde.", 500)


@consulta_bp.route('/animal/<int:id_animal>', methods=['GET'])
def get_consultas_por_animal(id_animal):
    try:
        consultas = ConsultaService.buscar_por_animal(id_animal)
        return jsonify(consultas), 200
    except Exception as e:
        return formatar_resposta_erro("Erro ao buscar consultas do animal.", 500)


@consulta_bp.route('/funcionario/<int:id_funcionario>', methods=['GET'])
def get_consultas_por_funcionario(id_funcionario):
    try:
        consultas = ConsultaService.buscar_por_funcionario(id_funcionario)
        return jsonify(consultas), 200
    except Exception as e:
        return formatar_resposta_erro("Erro ao buscar consultas do funcionário.", 500)


@consulta_bp.route('', methods=['POST'])
def cadastrar_consulta():
    try:
        data = request.get_json()

        id_animal = data.get('id_animal')
        id_funcionario = data.get('id_funcionario')
        data_consulta_str = data.get('data_consulta')
        diagnostico = data.get('diagnostico')
        observacoes = data.get('observacoes')

        # Valida a data da consulta antes de passar para o service
        data_consulta = validar_data_consulta(data_consulta_str)

        consulta = ConsultaService.cadastrar_consulta(id_animal, id_funcionario, data_consulta, diagnostico, observacoes)
        return jsonify(consulta.to_dict()), 201
    except ConsultaExistenteException as e:
        return formatar_resposta_erro(str(e), 409)
    except ValueError as e:
        return formatar_resposta_erro(f"Erro de validação: {str(e)}", 400)
    except Exception as e:
        return formatar_resposta_erro("Erro inesperado. Tente novamente mais tarde.", 500)


@consulta_bp.route('/<int:id_consulta>', methods=['PUT'])
def atualizar_consulta(id_consulta):
    try:
        data = request.get_json()

        data_consulta_str = data.get('data_consulta')
        diagnostico = data.get('diagnostico')
        observacoes = data.get('observacoes')

        # Valida a data da consulta
        data_consulta = validar_data_consulta(data_consulta_str)

        consulta_atualizada = ConsultaService.atualizar_consulta(id_consulta, data_consulta, diagnostico, observacoes)
        return jsonify(consulta_atualizada.to_dict()), 200
    except ConsultaNaoEncontradaException as e:
        return formatar_resposta_erro(str(e), 404)
    except ValueError as e:
        return formatar_resposta_erro(f"Erro de validação: {str(e)}", 400)
    except Exception as e:
        return formatar_resposta_erro("Erro inesperado. Tente novamente mais tarde.", 500)


@consulta_bp.route('/<int:id_consulta>', methods=['DELETE'])
def deletar_consulta(id_consulta):
    try:
        ConsultaService.deletar_consulta(id_consulta)
        return jsonify({"message": "Consulta excluída com sucesso."}), 204
    except ConsultaNaoEncontradaException as e:
        return formatar_resposta_erro(str(e), 404)
    except Exception as e:
        return formatar_resposta_erro("Erro inesperado. Tente novamente mais tarde.", 500)
