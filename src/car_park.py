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

    def add_car(self, plate):
        self.plates.append(plate)
        #self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        #self.update_displays()

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)




car1 = CarPark(location='San Francisco', capacity=1, plates=[], sensors=[], displays=[])
sens1 = Sensor(id=1, is_active=True, car_park=True)
display1 = Display(id="Display 1:", car_park=2, message="Welcome to the car park", is_on=True)
car1.register(sens1)
car1.register(display1)
plate1 = "12345"
plate2 = "56789"
plate3 = "ABCDEFGHIJKLMNO"
car1.add_car(plate1)
car1.add_car(plate2)
car1.add_car(plate3)
print(car1.available_bays)