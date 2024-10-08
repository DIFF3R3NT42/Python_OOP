from project.dark_knigth import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {BladeKnight.__name__} has level {self.level}"
