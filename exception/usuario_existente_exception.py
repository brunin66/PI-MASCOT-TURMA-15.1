class UsuarioExistenteException(Exception):
    def __init__(self, message="Usuário já existente"):
        self.message = message
        super().__init__(self.message)