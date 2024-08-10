from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
            else:
                return "Pokemon is not caught"

    def trainer_data(self) -> str:
        pokemon_details = "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)
        return (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n"
                f"{pokemon_details}")
