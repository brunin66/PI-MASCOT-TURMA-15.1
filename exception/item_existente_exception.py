class ItemExistenteException(Exception):
    def __init__(self, message="Item já cadastrado"):
        self.message = message
        super().__init__(self.message)