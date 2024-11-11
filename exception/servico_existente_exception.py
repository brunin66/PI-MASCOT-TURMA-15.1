class ServicoExistenteException(Exception):
    def __init__(self, message="Serviço já existente"):
        self.message = message
        super().__init__(self.message)