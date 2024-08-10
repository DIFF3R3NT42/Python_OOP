from project.soccer_player import SoccerPlayer
import unittest


class TestSoccerPlayer(unittest.TestCase):

    def setUp(self):
        """Set up a SoccerPlayer instance for testing."""
        self.player = SoccerPlayer("Lionel Messi", 34, 700, "Barcelona")

    def test_initial_values(self):
        """Test the initial values of the soccer player."""
        self.assertEqual(self.player.name, "Lionel Messi")
        self.assertEqual(self.player.age, 34)
        self.assertEqual(self.player.goals, 700)
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(self.player.achievements, {})

    def test_invalid_name_too_short(self):
        """Test setting a name that is too short raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.player.name = "Messi"
        self.assertEqual(str(context.exception), "Name should be more than 5 symbols!")

    def test_invalid_age_too_young(self):
        """Test setting an age below 16 raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.player.age = 15
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

    def test_goals_set_negative(self):
        """Test setting negative goals sets it to zero."""
        self.player.goals = -10
        self.assertEqual(self.player.goals, 0)

    def test_invalid_team(self):
        """Test setting an invalid team raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.player.team = "Invalid Team"
        self.assertEqual(str(context.exception),
                         "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")

    def test_change_team_success(self):
        """Test changing to a valid team."""
        result = self.player.change_team("Real Madrid")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "Real Madrid")

    def test_change_team_invalid(self):
        """Test changing to an invalid team returns error message."""
        result = self.player.change_team("Invalid Team")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement(self):
        """Test adding a new achievement."""
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 1)

    def test_add_existing_achievement(self):
        """Test adding an existing achievement increments the count."""
        self.player.add_new_achievement("Ballon d'Or")
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 2)

    def test_compare_players(self):
        """Test comparing players based on goals."""
        player2 = SoccerPlayer("Cristiano Ronaldo", 36, 800, "Juventus")
        result = self.player < player2
        self.assertEqual(result, "Cristiano Ronaldo is a top goal scorer! S/he scored more than Lionel Messi.")


if __name__ == '__main__':
    unittest.main()
