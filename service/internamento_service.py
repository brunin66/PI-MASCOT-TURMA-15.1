from repository.internamento_repository import InternamentoRepository
from exception.internamento_exception import InternamentoException
from datetime import datetime

class InternamentoService:

    @staticmethod
    def buscar_por_id(id_internamento):
        """Busca um internamento pelo ID. Lança um erro se não encontrado."""
        internamento = InternamentoRepository.get_by_id(id_internamento)
        if not internamento:
            raise ValueError("Internamento não encontrado.")
        return internamento

    @staticmethod
    def buscar_todos():
        """Busca todos os internamentos e retorna uma lista de dicionários."""
        internamentos = InternamentoRepository.get_all()
        return [internamento.to_dict() for internamento in internamentos]

    @staticmethod
    def buscar_por_animal(id_animal):
        """Busca todos os internamentos de um animal específico."""
        internamentos = InternamentoRepository.get_by_animal(id_animal)
        return [internamento.to_dict() for internamento in internamentos]

    @staticmethod
    def buscar_por_funcionario(id_funcionario):
        """Busca todos os internamentos realizados por um funcionário específico."""
        internamentos = InternamentoRepository.get_by_funcionario(id_funcionario)
        return [internamento.to_dict() for internamento in internamentos]

    @staticmethod
    def cadastrar_internamento(internamento):
        """Cadastra um novo internamento, realizando validações de dados."""
        if not internamento.motivo_internamento or len(internamento.motivo_internamento) < 5:
            raise ValueError("Motivo do internamento deve ter no mínimo 5 caracteres.")
        
        if internamento.status not in ['Ativo', 'Finalizado']:
            raise ValueError("Status inválido. O status deve ser 'Ativo' ou 'Finalizado'.")

        # Verificar se a data de internamento não está no futuro
        if internamento.data_internamento > datetime.utcnow():
            raise ValueError("Data de internamento não pode ser no futuro.")

        return InternamentoRepository.create(internamento)

    @staticmethod
    def atualizar_internamento(internamento):
        """Atualiza um internamento existente."""
        # Verificar se o internamento existe
        existing_internamento = InternamentoRepository.get_by_id(internamento.id_internamento)
        if not existing_internamento:
            raise ValueError("Internamento não encontrado.")
        
        if internamento.status not in ['Ativo', 'Finalizado']:
            raise ValueError("Status inválido. O status deve ser 'Ativo' ou 'Finalizado'.")
        
        # Atualiza o internamento
        return InternamentoRepository.update(internamento)

    @staticmethod
    def finalizar_internamento(id_internamento):
        """Finaliza um internamento, alterando o status e registrando a data de saída."""
        internamento = InternamentoRepository.get_by_id(id_internamento)
        if not internamento:
            raise ValueError("Internamento não encontrado.")
        
        # Atualizando o status para 'Finalizado' e registrando a data de saída
        internamento.status = 'Finalizado'
        internamento.data_saida = datetime.utcnow()
        
        return InternamentoRepository.update(internamento)

    @staticmethod
    def excluir_internamento(id_internamento):
        """Exclui um internamento."""
        return InternamentoRepository.delete(id_internamento)
