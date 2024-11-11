from repository.funcionario_repository import FuncionarioRepository
from entity.funcionario import Funcionario
from exception.funcionario_existente_exception import FuncionarioExistenteException
from exception.funcionario_email_existente_exception import FuncionarioEmailExistenteException

class FuncionarioService:

    @staticmethod
    def buscar_por_id(id):
        #Busca um funcionário pelo ID. Lança um erro se o funcionário não existir
        funcionario = FuncionarioRepository.get_by_id(id)
        if not funcionario:
            raise ValueError("Funcionário não cadastrado")
        return funcionario
        
    @staticmethod
    def buscar_todos():
        #Busca todos os funcionários e os retorna como uma lista de dicionários
        funcionarios = FuncionarioRepository.get_all()

        return [funcionario.to_dict() for funcionario in funcionarios] 
    
    @staticmethod
    def verificar_email_existente(email)-> bool:
        emails = FuncionarioRepository.get_by_email(email)
        return len(emails) > 0

    
    @staticmethod
    def cadastrar_funcionario(funcionario):
        #Cadastra um novo funcionário se o nome tiver pelo menos 3 caracteres
        if len(funcionario.nome) < 3:
            raise ValueError("Nome do funcionário menor que 3 caracteres")
        
        if FuncionarioService.verificar_email_existente(funcionario.email):
            raise FuncionarioEmailExistenteException("Email do funcionario ja em uso")
        
        return FuncionarioRepository.create(funcionario)
    @staticmethod
    def atualizar_funcionario(funcionario):
        #Atualiza as informações de um funcionário existente."""
        if len(funcionario.nome) < 3:
            raise ValueError("Nome do funcionário menor que 3 caracteres")
        
        # Verifica se o email é único (exceto para o próprio funcionário)
        funcionario_existente = FuncionarioRepository.get_by_id(funcionario.id)
        if funcionario_existente.email != funcionario.email and FuncionarioService.verificar_email_existente(funcionario.email):
            raise FuncionarioEmailExistenteException("Email do funcionário já em uso")

        return FuncionarioRepository.funcionario_update(funcionario)

    @staticmethod
    def deletar_funcionario(id):
        #Exclui um funcionário do banco de dados pelo ID.
        return FuncionarioRepository.funcionario_delete(id)