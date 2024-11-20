import unittest

from display import Display

from car_park import CarPark


class TestDisplay(unittest.TestCase):
    """
    Here we are going to set up and test a display object.
    We are going to test the initialization of the display object, including its attributes.
    And test the update method.
    """
    def setUp(self):
        """
        Here we set up an instance of a display with arguments we want to be initialized when the object is
        instantiated, including a CarPark object with it's own arguments.
        """
        self.display = Display(identity=1, message="welcome to the car park", is_on=True,
                               car_park=CarPark(capacity=10, location="ridgeracer"))

    def test_display_initialized_with_all_attributes(self):
        """
        Here we test that the attributes have been initialized properly.
        We test to see the following;
            self.display is an instance of a Display object.
            self.display.identity is equal to 1
            self.display.message is equal to "welcome to the car park"
            self.display.is_on is equal to True
            and that self.display.car_park is an instance of a CarPark object
        """
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.identity, 1)
        self.assertEqual(self.display.message, "welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        """
        Here we are testing the update method of the Display object.
        The update method is going to update the data variable with is a dictionary.
        here we set the key (in the key, value) to "message" and the value to that key: "goodbye"
        and the self.message attribute in the display object is set to the value
        We then test to see that self.display.message variable is equal to the string "goodbye"
        """
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")
