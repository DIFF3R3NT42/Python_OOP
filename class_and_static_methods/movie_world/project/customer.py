from typing import List


class Customer:
    def __init__(self, name: str, age: int, identification: int):
        self.name = name
        self.age = age
        self.id = identification
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented"
                f" DVD's ({', '.join(d.name for d in self.rented_dvds)})")
