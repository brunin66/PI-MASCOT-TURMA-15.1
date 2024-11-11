class MaterialExistenteException(Exception):
    def __init__(self, message="Material já cadastrado"):
        self.message = message
        super().__init__(self.message)