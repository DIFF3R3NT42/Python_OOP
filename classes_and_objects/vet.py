class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name) -> str:
        if Vet.space > 0:
            Vet.space -= 1
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name) -> str:
        if animal_name in Vet.animals and animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
