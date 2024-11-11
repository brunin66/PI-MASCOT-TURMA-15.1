from flask import Blueprint, jsonify, request
from service.usuario_service import UsuarioService
from entity.usuario import Usuario
from exception.usuario_existente_exception import UsuarioExistenteException
from exception.usuario_login_existente_exception import UsuarioLoginExistenteException

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    # Obtém um usuário pelo ID
    try:
        usuario = UsuarioService.buscar_por_id(id_usuario)
        return jsonify(usuario.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

@usuario_bp.route('', methods=['GET'])
def get_usuarios():
    # Obtém todos os usuários
    usuarios = UsuarioService.buscar_todos()
    return jsonify(usuarios)

@usuario_bp.route('', methods=['POST'])
def cadastrar_usuario():
    # Cadastra um novo usuário
    data = request.get_json()
    usuario = Usuario(
        id_funcionario=data['id_funcionario'],  # Referência ao funcionário
        login=data['login'],
        senha=data['senha'],
        perfil=data['perfil']
        # Adicione outros atributos necessários para o Usuario aqui
    )
    
    try:
        usuario_salvo = UsuarioService.cadastrar_usuario(usuario)
        return jsonify(usuario_salvo.to_dict()), 201
    except UsuarioLoginExistenteException as em:
        print(f'Caiu na Exception do login! error : {em}')
        return jsonify({"Error": str(em)}), 409
    except UsuarioExistenteException as ce:
        return jsonify({"Error": str(ce)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500


@usuario_bp.route('/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    # Atualiza as informações de um usuário existente.
    data = request.get_json()
    usuario = Usuario(
        id_usuario=id_usuario,  # Usar o ID fornecido na URL
        login=data['login'],
        senha=data['senha'],
        perfil=data['perfil']
        # Adicione outros atributos necessários para o Usuario aqui
    )
    
    try:
        usuario_atualizado = UsuarioService.atualizar_usuario(usuario)
        return jsonify(usuario_atualizado.to_dict()), 200
    except UsuarioLoginExistenteException as em:
        return jsonify({"Error": str(em)}), 409
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500

@usuario_bp.route('/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    # Exclui um usuário pelo ID
    try:
        if UsuarioService.deletar_usuario(id_usuario):
            return jsonify({"Message": "Usuário excluído com sucesso."}), 204
        else:
            return jsonify({"Error": "Falha ao excluir o usuário."}), 400
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as ex:
        return jsonify({"Error": "Erro inesperado, tente novamente mais tarde."}), 500