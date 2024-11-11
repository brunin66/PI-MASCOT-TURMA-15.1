from repository.consulta_repository import ConsultaRepository
from entity.consulta import Consulta
from exception.consulta_existente_exception import ConsultaExistenteException
from exception.consulta_nao_encontrada_exception import ConsultaNaoEncontradaException
from datetime import datetime

class ConsultaService:

    @staticmethod
    def buscar_por_id(id_consulta):
        # Busca uma consulta pelo ID e lança um erro se não encontrado
        consulta = ConsultaRepository.get_by_id(id_consulta)
        if not consulta:
            raise ConsultaNaoEncontradaException(f"Consulta com ID {id_consulta} não encontrada.")
        return consulta

    @staticmethod
    def buscar_todas():
        # Busca todas as consultas
        consultas = ConsultaRepository.get_all()
        return [consulta.to_dict() for consulta in consultas]
    
    @staticmethod
    def buscar_por_animal(id_animal):
        # Busca todas as consultas de um animal específico
        consultas = ConsultaRepository.get_by_animal(id_animal)
        return [consulta.to_dict() for consulta in consultas]

    @staticmethod
    def buscar_por_funcionario(id_funcionario):
        # Busca todas as consultas de um funcionário específico
        consultas = ConsultaRepository.get_by_funcionario(id_funcionario)
        return [consulta.to_dict() for consulta in consultas]
    
    @staticmethod
    def cadastrar_consulta(id_animal, id_funcionario, data_consulta, diagnostico=None, observacoes=None):
        # Cadastra uma nova consulta
        if not isinstance(data_consulta, datetime):
            raise ValueError("A data da consulta precisa ser um objeto datetime.")

        # Verifica se a consulta já existe (se a mesma data e os mesmos IDs já tiverem sido registrados)
        consultas_existentes = ConsultaRepository.get_by_animal(id_animal)
        for consulta in consultas_existentes:
            if consulta.data_consulta == data_consulta:
                raise ConsultaExistenteException(f"Já existe uma consulta marcada para este animal na data {data_consulta}.")

        consulta = Consulta(
            id_animal=id_animal,
            id_funcionario=id_funcionario,
            data_consulta=data_consulta,
            diagnostico=diagnostico,
            observacoes=observacoes
        )
        
        return ConsultaRepository.create(consulta)

    @staticmethod
    def atualizar_consulta(id_consulta, data_consulta, diagnostico=None, observacoes=None):
        # Atualiza uma consulta existente
        consulta = ConsultaService.buscar_por_id(id_consulta)  # Verifica se a consulta existe
        
        if not isinstance(data_consulta, datetime):
            raise ValueError("A data da consulta precisa ser um objeto datetime.")
        
        # Atualiza os campos da consulta
        consulta.data_consulta = data_consulta
        consulta.diagnostico = diagnostico
        consulta.observacoes = observacoes
        
        return ConsultaRepository.update(consulta)

    @staticmethod
    def deletar_consulta(id_consulta):
        # Exclui uma consulta pelo ID
        consulta = ConsultaService.buscar_por_id(id_consulta)  # Verifica se a consulta existe
        return ConsultaRepository.delete(id_consulta)
