class ServicoNaoEncontradoException(Exception):
    def __init__(self, message="Serviço não encontrado! "):
        self.message = message
        super().__init__(self.message)