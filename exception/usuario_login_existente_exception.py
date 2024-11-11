class UsuarioLoginExistenteException(Exception):
    def __init__(self, message="Login do usuário já em uso"):
        self.message = message
        super().__init__(self.message)