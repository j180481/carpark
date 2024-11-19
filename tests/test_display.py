import unittest

from display import Display

from car_park import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(identity=1, message="welcome to the car park", is_on=True,
                               car_park=CarPark(capacity=10, location="ridgeracer"))

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.identity, 1)
        self.assertEqual(self.display.message, "welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")
