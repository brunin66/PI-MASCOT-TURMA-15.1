from repository.cliente_repository import ClienteRepository
from entity.cliente import Cliente
from exception.cliente_existente_exception import ClienteExistenteException
from exception.cliente_email_existente_exception import ClienteEmailExistenteException

class ClienteService:

    @staticmethod
    def buscar_por_id(id):
        # Busca um cliente pelo ID. Lança um erro se o cliente não existir
        cliente = ClienteRepository.get_by_id(id)
        if not cliente:
            raise ValueError("Cliente não cadastrado")
        return cliente
        
    @staticmethod
    def buscar_todos():
        # Busca todos os clientes e os retorna como uma lista de dicionários
        clientes = ClienteRepository.get_all()

        return [cliente.to_dict() for cliente in clientes] 
    
    @staticmethod
    def verificar_email_existente(email) -> bool:
        emails = ClienteRepository.get_by_email(email)
        return len(emails) > 0

    @staticmethod
    def cadastrar_cliente(cliente):
        # Cadastra um novo cliente se o nome tiver pelo menos 3 caracteres
        if len(cliente.nome) < 3:
            raise ValueError("Nome do cliente menor que 3 caracteres")
        
        if ClienteService.verificar_email_existente(cliente.email):
            raise ClienteEmailExistenteException("Email do cliente já em uso")
        
        return ClienteRepository.create(cliente)
    @staticmethod
    def atualizar_cliente(cliente):
        #Atualiza as informações de um cliente existente.
        if len(cliente.nome) < 3:
            raise ValueError("Nome do cliente menor que 3 caracteres")
        
        # Verifica se o email é único (exceto para o próprio cliente)
        existing_cliente = ClienteRepository.get_by_id(cliente.id)
        if existing_cliente.email != cliente.email and ClienteService.verificar_email_existente(cliente.email):
            raise ClienteEmailExistenteException("Email do cliente já em uso")

        return ClienteRepository.update(cliente)
    
    @staticmethod
    def deletar_cliente(id):
        #Exclui um cliente do banco de dados pelo ID."""
        return ClienteRepository.delete(id)