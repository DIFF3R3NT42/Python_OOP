from project import player
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: list = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_to_remove = None
        for player in self.players:
            if player.name == player_name:
                player_to_remove = player
                break

        if player_to_remove:
            self.players.remove(player_to_remove)
            player_to_remove.guild = "Unaffiliated"
        else:
            return f"Player {player_name} is not in the guild."
    def guild_info(self) -> str:
        info = f"Guild: {self.name}\n"
        for player in self.players:
            info += player.player_info() + "\n"  # Add each player's info
        return info.strip()
