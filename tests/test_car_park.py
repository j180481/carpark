import unittest
from car_park import CarPark

from pathlib import Path


class TestCarPark(unittest.TestCase):
    """
    Here we are going to set up a CarPark class and test its initialization and attributes.
    And a variety of methods.
    """
    def setUp(self):
        """
        Here we set up an instance of a CarPark with arguments we want to be initialized when the object is
        instantiated, including a CarPark object with it's own arguments.
        And create a log file for each test.
        """
        self.log_file_name = Path("new_log.txt")
        self.car_park = CarPark("123 Example Street", 100, log_file=self.log_file_name)

    def test_car_park_initialized_with_all_attributes(self):
        """
        Here we are going to test the CarPark class initialization.
        Specifically testing that the attributes are initialized correctly.
        """
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path(self.log_file_name))

    def test_add_car(self):
        """
        Here we are going to test the CarPark class addition.
        We add the test plate "FAKE-001"
        Then we test that the plate can be found in the plates list.
        And test that the number of available bays is correct (99).
        """
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        """
        Here we are going to test the CarPark class removal.
        We add the fake plate "FAKE-001"
        Then we remove the fake plate "FAKE-001"
        Then we test that the plates list is empty.
        And test that the number of available bays is correct (100).
        """
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        """
        Here we are going to test the CarPark class overfilling.
        We add plates to capacity.
        Then test to make sure the number of available bays is correct (0)
        Then we add another plate to the plates list.
        And test that the number of available bays is still correct (0).
        Then we remove a plate from the plates list.
        And test that if we remove a plate from the list but the list still exceeds capacity, it doesnt change from 0.
        """
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        """
        Here we are going to test that if you try to remove a car that doesnt exist it raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        """
        Here we are testing that if you attempt to register an object which is neither a sensor or display, it will
        return a TypeError exception.
        In this case it is trying to register a variable containing the string "hello" - this should fail.
        """
        car_park_register_test = CarPark("123 Example Street", 100)
        string_object = "hello"
        with self.assertRaises(TypeError):
            car_park_register_test.register(string_object)

    def test_log_file_created(self):
        """
        Here we are going to test that a log file has been created when we initialize the CarPark class.
        """
        new_carpark = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        self.assertTrue(Path(self.log_file_name).exists())

    def tearDown(self):
        """
        This method is simply to remove the log file for clean testing purposes.
        :return:
        """
        Path(self.log_file_name).unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        """
        Here we are testing that when a car is "entering" that it is logged in a log file correctly.
        We add a car to the plates list.
        And then open the log file and test to make sure the strings "NEW-001", "entered" and "\n" are present
        in the file
        """
        self.car_park = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        """
        Here we are testing that when a car is "exiting" that it is logged ina  log file correctly.
        We add a car to the plates list.
        Then remove the plate from the plates list.
        Open the log file and test that the strings "NEW-001", "exited" and "\n" are present
        in the log file.
        """
        self.car_park = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate exited
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line


if __name__ == "__main__":
    unittest.main()
