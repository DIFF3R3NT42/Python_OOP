from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService", "SecondaryService"}
    VALID_ROBOT_TYPES = {"MaleRobot", "FemaleRobot"}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = None
        if service_type == "MainService":
            service = MainService(name)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = None
        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if not robot or not service:
            raise Exception("Robot or service does not exist!")

        if (isinstance(robot, MaleRobot) and not isinstance(service, MainService)) or \
           (isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService)):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = next((s for s in self.services if s.name == service_name), None)

        if not service:
            raise Exception("Service does not exist!")

        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = next((s for s in self.services if s.name == service_name), None)

        if not service:
            raise Exception("Service does not exist!")

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = next((s for s in self.services if s.name == service_name), None)

        if not service:
            raise Exception("Service does not exist!")

        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self) -> str:
        result = []
        for service in self.services:
            robot_names = " ".join(robot.name for robot in service.robots)
            result.append(f"{service.name} {service.__class__.__name__}:\nRobots: {robot_names}")
        return "\n".join(result)


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
