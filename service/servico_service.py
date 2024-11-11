from repository.servico_repository import ServicoRepository
from exception.servico_existente_exception import ServicoExistenteException
from exception.servico_nao_encontrado_exception import ServicoNaoEncontradoException


class ServicoService:

    @staticmethod
    def buscar_por_id(id_servico):
        # Busca um serviço pelo ID
        servico = ServicoRepository.get_by_id(id_servico)
        if not servico:
            raise ServicoNaoEncontradoException("Serviço não encontrado.")
        return servico
    
    @staticmethod
    def buscar_todos():
        # Busca todos os serviços e retorna uma lista de dicionários
        servicos = ServicoRepository.get_all()
        return [servico.to_dict() for servico in servicos]
    
    @staticmethod
    def verificar_servico_existente(nome):
        # Verifica se um serviço com o mesmo nome já existe
        servico = ServicoRepository.get_by_nome(nome)
        return servico is not None

    @staticmethod
    def cadastrar_servico(servico):
        # Cadastra um novo serviço
        if len(servico.nome) < 3:
            raise ValorInvalidoException("O nome do serviço deve ter pelo menos 3 caracteres.")
        
        if ServicoService.verificar_servico_existente(servico.nome):
            raise ServicoExistenteException(f"Já existe um serviço com o nome {servico.nome}.")
        
        return ServicoRepository.create(servico)
    
    @staticmethod
    def atualizar_servico(servico):
        # Atualiza as informações de um serviço existente
        if len(servico.nome) < 3:
            raise ValorInvalidoException("O nome do serviço deve ter pelo menos 3 caracteres.")
        
        # Verifica se o serviço existe
        servico_existente = ServicoRepository.get_by_id(servico.id_servico)
        if not servico_existente:
            raise ServicoNaoEncontradoException("Serviço não encontrado para atualização.")
        
        # Atualiza e salva
        return ServicoRepository.update(servico)
    
    @staticmethod
    def deletar_servico(id_servico):
        # Deleta um serviço pelo ID
        servico = ServicoRepository.get_by_id(id_servico)
        if not servico:
            raise ServicoNaoEncontradoException("Serviço não encontrado para exclusão.")
        
        return ServicoRepository.delete(id_servico)
