from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

#If the json file doesnt exist, it will create the carpark object with this configuration and then write it to json.
#else, it will create the carpark via the config file.
if not Path("config.json").exists():
    car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
    car_park.write_config()
else:
    car_park = CarPark.load_config()

entry_sensor = EntrySensor(identity=1, is_active=True, car_park=car_park)

exit_sensor = ExitSensor(identity=2, is_active=True, car_park=car_park)

display = Display(identity=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)
print(display)

car_park.register(entry_sensor)

car_park.register(exit_sensor)

car_park.register(display)

for i in range(10):
    entry_sensor.detect_vehicle()

for i in range(2):
    exit_sensor.detect_vehicle()
