class AnimalNaoEncontradoException(Exception):
    def __init__(self, message="Animal não encontrado! "):
        self.message = message
        super().__init__(self.message)