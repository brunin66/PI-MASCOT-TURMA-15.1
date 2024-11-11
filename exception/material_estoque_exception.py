class MaterialEstoqueException(Exception):
    def __init__(self, message="Material já no estoque"):
        self.message = message
        super().__init__(self.message)