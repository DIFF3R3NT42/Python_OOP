from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):

    def test_init_valid_data(self):
        """Tests initialization with valid data."""
        player = TennisPlayer("Roger Federer", 41, 1234.5)
        self.assertEqual(player.name, "Roger Federer")
        self.assertEqual(player.age, 41)
        self.assertEqual(player.points, 1234.5)
        self.assertEqual(player.wins, [])

    def test_init_name_too_short(self):
        """Tests initialization with a name less than or equal to 2 characters."""
        with self.assertRaises(ValueError) as cm:
            TennisPlayer("RF", 41, 1234.5)
        self.assertEqual(str(cm.exception), "Name should be more than 2 symbols!")

    def test_init_age_less_than_18(self):
        """Tests initialization with an age less than 18."""
        with self.assertRaises(ValueError) as cm:
            TennisPlayer("Rafael Nadal", 17, 5678.9)
        self.assertEqual(str(cm.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_unique_tournament(self):
        """Tests adding a new, unique tournament win."""
        player = TennisPlayer("Novak Djokovic", 35, 8901.2)
        result = player.add_new_win("Wimbledon 2024")
        self.assertEqual(result, None)
        self.assertEqual(player.wins, ["Wimbledon 2024"])

    def test_add_new_win_existing_tournament(self):
        """Tests adding an already existing tournament win."""
        player = TennisPlayer("Andy Murray", 36, 3456.7)
        player.add_new_win("Australian Open 2024")
        result = player.add_new_win("Australian Open 2024")
        self.assertEqual(result, "Australian Open 2024 has been already added to the list of wins!")
        self.assertEqual(player.wins, ["Australian Open 2024"])

    def test_lt_higher_points(self):
        """Tests __lt__ when the other player has higher points."""
        player1 = TennisPlayer("Serena Williams", 41, 7890.1)
        player2 = TennisPlayer("Iga Swiatek", 21, 9876.5)
        result = player1 < player2
        self.assertEqual(result, f'{player2.name} is a top seeded player and he/she is better than {player1.name}')

    def test_lt_lower_points(self):
        """Tests __lt__ when the current player has higher points."""
        player1 = TennisPlayer("Stefanos Tsitsipas", 24, 10234.9)
        player2 = TennisPlayer("Daniil Medvedev", 26, 8765.4)
        result = player1 < player2
        self.assertEqual(result, f'{player1.name} is a better player than {player2.name}')

    def test_str(self):
        """Tests the __str__ method."""
        player = TennisPlayer("Alexander Zverev", 25, 6543.2)
        player.add_new_win("French Open 2024")
        expected_string = f"Tennis Player: Alexander Zverev\n" \
                          f"Age: 25\n" \
                          f"Points: 6543.2\n" \
                          f"Tournaments won: French Open 2024"
        self.assertEqual(str(player), expected_string)


if __name__ == '__main__':
    unittest.main()
