from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):

    def setUp(self):
        """Set up a Robot instance for testing."""
        self.robot = Robot("R001", "Military", 100, 1000.0)

    def test_initial_values(self):
        """Test the initial values of the robot."""
        self.assertEqual(self.robot.robot_id, "R001")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 1000.0)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_invalid_category(self):
        """Test setting an invalid category raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.robot.category = "Invalid"
        self.assertEqual(str(context.exception),
                         "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_negative_price(self):
        """Test setting a negative price raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.robot.price = -200.0
        self.assertEqual(str(context.exception), "Price cannot be negative!")

    def test_upgrade_robot(self):
        """Test upgrading the robot with a new hardware component."""
        result = self.robot.upgrade("Arm", 50.0)
        self.assertEqual(result, "Robot R001 was upgraded with Arm.")
        self.assertIn("Arm", self.robot.hardware_upgrades)
        self.assertEqual(self.robot.price, 1075.0)

    def test_upgrade_duplicate(self):
        """Test upgrading with a duplicate component does not change state."""
        self.robot.upgrade("Leg", 30.0)
        result = self.robot.upgrade("Leg", 30.0)
        self.assertEqual(result, "Robot R001 was not upgraded.")

    def test_update_robot(self):
        """Test updating the robot with a new software version."""
        result = self.robot.update(1.1, 10)
        self.assertEqual(result, "Robot R001 was updated to version 1.1.")
        self.assertIn(1.1, self.robot.software_updates)
        self.assertEqual(self.robot.available_capacity, 90)

    def test_update_lower_version(self):
        """Test attempting to update with a lower version."""
        self.robot.update(1.0, 20)
        result = self.robot.update(0.9, 10)
        self.assertEqual(result, "Robot R001 was not updated.")

    def test_update_insufficient_capacity(self):
        """Test attempting to update with insufficient capacity."""
        result = self.robot.update(2.0, 110)
        self.assertEqual(result, "Robot R001 was not updated.")

    def test_compare_robots(self):
        """Test comparing robots based on price."""
        robot2 = Robot("R002", "Military", 100, 1200.0)
        robot3 = Robot("R003", "Education", 100, 1000.0)

        self.assertEqual(self.robot > robot2, "Robot with ID R001 is cheaper than Robot with ID R002.")
        self.assertEqual(robot2 > self.robot, "Robot with ID R002 is more expensive than Robot with ID R001.")
        self.assertEqual(self.robot > robot3, "Robot with ID R001 costs equal to Robot with ID R003.")


if __name__ == '__main__':
    unittest.main()
