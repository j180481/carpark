from sensor import Sensor

from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Location: {self.location}, Capacity: {self.capacity}'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)





car1 = CarPark(location='San Francisco', capacity=100, plates=[], sensors=[], displays=[])
sens1 = Sensor(id=1, is_active=True, car_park=True)
display1 = Display(id="Display 1:", car_park=2, message="Welcome to the car park", is_on=True)
car1.register(sens1)
car1.register(display1)
var1="jello"
car1.register(var1)