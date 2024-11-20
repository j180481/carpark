import json

from sensor import Sensor

from display import Display

from pathlib import Path
from datetime import datetime


class CarPark:
    """
    Represents a car park, including the location and capacity of car park. This class will also manage sensors,
    displays, "leaving" and "entering" cars, predominantly.
    """
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt"),
                 config_file=Path("config.json")):
        """
        Here we initialize the object of a CarPark object with the following parameters;
        :param location: variable containing a string of the location of the carpark
        :param capacity: variable containing an integer representing the capacity of the car park
        :param plates: a list of "plates" of all cars currently in the car park
        :param sensors: a list of sensors which we register with the register method
        :param displays: a list of displays which we register with the register method
        :param log_file: Path for the log file which will record the cars entering or leaving
        :param config_file: path for the config file of a carpark
        """
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch(exist_ok=True)
        self.config_file = config_file

    def __str__(self):
        """
        If we print an instance of a carpark object, it will return a string representation of the car park
        Specifically, it returns the location and capacity of the car park.
        """
        return f'Location: {self.location}, Capacity: {self.capacity}'

    def register(self, component):
        """
        The method which we use to "register" a sensor or display to the car park.
        It takes one parameter "component".
        Then we check if the component is an instance of a sensor or display.
        If it is a sensor it is appended to the attribute self.sensors list.
        if it is a display it is appended to the attribute self.displays list.
        If it is neither, it will raise a type error.
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
        Method we use to add a car to the car park.
        Accepts the parameter "plate".
        Adds the plate to the self.plates list
        calls the update_displays method to display car entered to user.
        Then logs the car activity.
        """
        self.plates.append(plate)
        self.update_displays()
        #print(f"Car {plate} entered")
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
        Method we use to remove a car from the car park.
        Accepts the parameter "plate".
        Removes the plate from the self.plates list
        calls the update_displays method to display car exited to user.
        Then logs the car activity.
        """
        self.plates.remove(plate)
        self.update_displays()
        #print(f"Car {plate} exited")
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        """
        Here we use this method to calculate the number of available bays.
        if the number of plates in the plates list exceeds the capacity, we return 0.
        Otherwise, we take the capacity of the car park and minus the number of plates in the plates list.
        Then return the integer.
        """
        if len(self.plates) > self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        """
        Updates the displays with current number of available bays and the current temperature.
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        """
        Here we log the car activity.
        :param plate: the plate detected
        :param action: whether they are entering or exiting
        Then we write the car activity to the log file, including the current date and time.
        """
        #print(f"Logging: {plate}, Action: {action}")
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        """
        Writes the current carpark configuration to a json file.
        :return:
        """
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location, "capacity": self.capacity, "log_file": str(self.log_file)}, f)

    @classmethod
    def load_config(cls, config_file=Path("config.json")):
        """
        We use this method to load the carpark configuration from a json file.
        :param config_file: is the path to the config file
        returns a config we can initialize a carpark with
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])


