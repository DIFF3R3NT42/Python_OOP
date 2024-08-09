class Pokemon:
    def __init__(self, name: object, health: int) -> None:
        self.name = name
        self.health = health

    def pokemon_details(self) -> str:
        return f"{self.name} with health {self.health}"

    def __str__(self) -> str:
        return self.pokemon_details()