from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    """
    An abstract base class for sensors
    """
    def __init__(self, identity, is_active, car_park):
        """
        Here we initialize the sensor and it's attributes via the following parameters
        :param identity: the sensor should initialize with a number to identify the sensor
        :param is_active: a boolean to indicate if the sensor is active
        :param car_park: the CarPark instance associated with the sensor
        """
        self.identity = identity
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        """
        If we print an instance of a sensor, it will return string representation of the sensor.
        Specifically, it returns the sensor identity number and whether it is active.
        """
        return f'Sensor {self.identity} is active: {self.is_active}'

    @abstractmethod
    def update_car_park(self, plate):
        """
        An abstract method to update the car park, and it takes one parameter; plate.
        It is expected that different sensors (sensor classes which inherit from Sensor)
         will implement this method uniquely.
        :param plate: plate number of the car to be updated within the carpark instance.
        """
        pass

    def _scan_plate(self):
        """
        Here we randomly generate a license plate and return it.
        """
        return 'FAKE-' + format(random.randint(0, 9999), '03d')

    def detect_vehicle(self):
        """
        Here we simulate the detection of the vehicle and return the plate.
        To do so, the _scan_plate() method is used to return a generate plate to the variable called "plate"
        Then we use the update_car_park(). How this method will be used depends on the class which has inherited
        from Sensor.
        """
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    """
    Subclass of Sensor to represent an entry sensor.
    """
    def update_car_park(self, plate):
        """
        Here we implement the abstract class update_car_park.
        If an entry sensor detects a plate, it calls the car_park.add_car method to add it to the car park.
        Specifically, adds the plate a list in the CarPark.
        And then prints a message to the user informing them a vehicle has been detected, and the vehicle plate.
        """
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    """
    Subclass of Sensor to represent an exit sensor.
    """
    def update_car_park(self, plate):
        """
        Here we implement the abstract class update_car_park.
        If an exit sensor detects a plate, it will call the car_park.remove_car method to remove it from the car park.
        Specifically, removes the plate a list in the CarPark.
        And then prints a message to the user informing them a vehicle has been detected leaving, and the vehicle plate.
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """
        Here we overwrite the base method to "scan" or randomly choose a plate from the list of plates in the car park.
        """
        return random.choice(self.car_park.plates)
