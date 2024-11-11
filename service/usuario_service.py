from repository.usuario_repository import UsuarioRepository
from entity.usuario import Usuario
from exception.usuario_existente_exception import UsuarioExistenteException
from exception.usuario_login_existente_exception import UsuarioLoginExistenteException

class UsuarioService:

    @staticmethod
    def buscar_por_id(id_usuario):
        # Busca um usuário pelo ID. Lança um erro se o usuário não existir
        usuario = UsuarioRepository.get_by_id(id_usuario)
        if not usuario:
            raise ValueError("Usuário não cadastrado")
        return usuario
        
    @staticmethod
    def buscar_todos():
        # Busca todos os usuários e os retorna como uma lista de dicionários
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def verificar_login_existente(login) -> bool:
        # Verifica se já existe um usuário com o login fornecido
        usuarios = UsuarioRepository.get_by_login(login)
        return usuarios is not None

    @staticmethod
    def cadastrar_usuario(usuario):
        # Cadastra um novo usuário, se o login tiver pelo menos 3 caracteres
        if len(usuario.login) < 3:
            raise ValueError("Login do usuário menor que 3 caracteres")
        
        if UsuarioService.verificar_login_existente(usuario.login):
            raise UsuarioLoginExistenteException("Login do usuário já em uso")
        
        return UsuarioRepository.create(usuario)

    @staticmethod
    def atualizar_usuario(usuario):
        # Atualiza as informações de um usuário existente
        if len(usuario.login) < 3:
            raise ValueError("Login do usuário menor que 3 caracteres")
        
        # Verifica se o login é único (exceto para o próprio usuário)
        usuario_existente = UsuarioRepository.get_by_id(usuario.id_usuario)
        if usuario_existente.login != usuario.login and UsuarioService.verificar_login_existente(usuario.login):
            raise UsuarioLoginExistenteException("Login do usuário já em uso")

        return UsuarioRepository.usuario_update(usuario)

    @staticmethod
    def deletar_usuario(id_usuario):
        # Exclui um usuário do banco de dados pelo ID
        return UsuarioRepository.usuario_delete(id_usuario)