import unittest

import random

from car_park import CarPark

from sensor import EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):

    def setUp(self):
        self.entry_sensor = EntrySensor(identity=1, is_active=True, car_park=CarPark(capacity=10, location="ridgeracer"))
        self.exit_sensor = ExitSensor(identity=2, is_active=True, car_park=CarPark(capacity=10, location="ridgeracer"))

    def test_sensor_initialized_with_all_attributes(self):
        #testing that the sensors are initialized properly
        self.assertEqual(self.entry_sensor.identity, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

        self.assertEqual(self.exit_sensor.identity, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_entry_sensor_detect_vehicle(self):
        #using random and it's built in function seed so we can generate the same "random" result for testing
        random.seed(0)
        #running the script i found this is the plate number it will generate with the seed set to 0
        plate = "FAKE-6311"

        self.entry_sensor.detect_vehicle()
        #then we check to see that the plate variable is in the car_park plates attribute containing the list of plates
        self.assertIn(plate, self.entry_sensor.car_park.plates)

    def test_exit_sensor_detect_vehicle(self):
        #using the previous test as a reference simply for clean output i have matched the plate variable
        plate = "FAKE-6311"

        #since we are specifically testing the exit sensor, i manually add the fake plate for this test purpose specifically
        self.exit_sensor.car_park.plates = [plate]
        #And here, i'm checking to make sure the fake plate is added
        self.assertIn(plate, self.exit_sensor.car_park.plates)

        #calling the exit sensors detect_vehicle method, which should remove the plate
        self.exit_sensor.detect_vehicle()

        #and lastly, checking to make sure the plate is not in the list and removed as expected
        self.assertNotIn(plate, self.exit_sensor.car_park.plates)


if __name__ == "__main__":
    unittest.main()