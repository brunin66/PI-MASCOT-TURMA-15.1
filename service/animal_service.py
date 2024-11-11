from repository.animal_repository import AnimalRepository
from exception.animal_existente_exception import AnimalExistenteException
from exception.animal_nao_encontrado_exception import AnimalNaoEncontradoException

class AnimalService:

    @staticmethod
    def buscar_por_id(id_animal):
        # Busca um animal pelo ID. Lança um erro se o animal não existir
        animal = AnimalRepository.get_by_id(id_animal)
        if not animal:
            raise AnimalNaoEncontradoException("Animal não encontrado.")
        return animal

    @staticmethod
    def buscar_todos():
        # Busca todos os animais e os retorna como uma lista de dicionários
        animais = AnimalRepository.get_all()
        return [animal.to_dict() for animal in animais]

    @staticmethod
    def buscar_por_cliente(id_cliente):
        # Busca todos os animais de um cliente
        animais = AnimalRepository.get_by_cliente(id_cliente)
        return [animal.to_dict() for animal in animais]

    @staticmethod
    def cadastrar_animal(animal):
        # Cadastra um novo animal
        if len(animal.nome) < 3:
            raise ValueError("Nome do animal deve ter pelo menos 3 caracteres.")
        
        # Chama o repository para salvar o animal
        try:
            animal_salvo = AnimalRepository.create(animal)
            if not animal_salvo:
                raise Exception("Erro ao salvar o animal.")
            return animal_salvo
        except AnimalExistenteException as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao cadastrar o animal: {str(e)}")

    @staticmethod
    def atualizar_animal(animal):
        # Atualiza as informações de um animal existente
        if len(animal.nome) < 3:
            raise ValueError("Nome do animal deve ter pelo menos 3 caracteres.")
        
        # Chama o repository para atualizar o animal
        try:
            animal_atualizado = AnimalRepository.update(animal)
            if not animal_atualizado:
                raise AnimalNaoEncontradoException("Animal não encontrado para atualização.")
            return animal_atualizado
        except AnimalNaoEncontradoException as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao atualizar o animal: {str(e)}")

    @staticmethod
    def deletar_animal(id_animal):
        # Exclui um animal do banco de dados
        try:
            sucesso = AnimalRepository.delete(id_animal)
            if not sucesso:
                raise AnimalNaoEncontradoException("Animal não encontrado para exclusão.")
            return {"message": "Animal excluído com sucesso."}
        except AnimalNaoEncontradoException as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao excluir o animal: {str(e)}")
