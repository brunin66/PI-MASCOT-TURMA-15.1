from entity.animal import Animal
from db import db
from exception.animal_existente_exception import AnimalExistenteException

class AnimalRepository:

    @staticmethod
    def get_all():
        # Retorna todos os animais
        return Animal.query.all()

    @staticmethod
    def get_by_id(id_animal):
        # Retorna um animal pelo ID
        return Animal.query.get(id_animal)

    @staticmethod
    def get_by_cliente(id_cliente):
        # Retorna todos os animais de um cliente específico
        return Animal.query.filter_by(id_cliente=id_cliente).all()

    @staticmethod
    def create(animal):
        # Cria um novo animal no banco de dados
        try:
            # Verifica se o animal já existe (exemplo: com o mesmo nome para o cliente)
            existing_animal = AnimalRepository.get_by_cliente(animal.id_cliente)
            for a in existing_animal:
                if a.nome == animal.nome:  # Verificação simples, você pode melhorar a lógica
                    raise AnimalExistenteException(f"O animal com nome '{animal.nome}' já existe para este cliente.")
            
            db.session.add(animal)
            db.session.commit()
            return animal
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            return None

    @staticmethod
    def update(animal):
        # Atualiza os dados de um animal
        try:
            existing_animal = AnimalRepository.get_by_id(animal.id_animal)
            if not existing_animal:
                raise ValueError("Animal não encontrado.")

            # Atualiza os campos
            existing_animal.nome = animal.nome
            existing_animal.tipo = animal.tipo
            existing_animal.raca = animal.raca
            existing_animal.data_nascimento = animal.data_nascimento
            existing_animal.sexo = animal.sexo
            existing_animal.peso = animal.peso

            db.session.commit()
            return existing_animal
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            return None

    @staticmethod
    def delete(id_animal):
        # Exclui um animal pelo ID
        try:
            animal = AnimalRepository.get_by_id(id_animal)
            if not animal:
                raise ValueError("Animal não encontrado.")

            db.session.delete(animal)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            return False
