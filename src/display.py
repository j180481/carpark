class Display:
    """
    Represents a display for a carpark.
    """
    def __init__(self, identity, car_park, message="", is_on=False):
        """
        Here we initialize the display with its attributes via the following parameters;
        :param identity: an integer identifying the display (1, 2, 3, etc)
        :param car_park: CarPark instance which the display will be associated with
        :param message: string message which can be displayed to user
        :param is_on: boolean to indicate if the display is on or off
        """
        self.identity = identity
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        """
        If we print an instance of a Display it should return a string.
        Specifically, a string communicating the displays "identity" and "messagee"
        """
        return f'Display {self.identity}: {self.message}'

    def update(self, data):
        """
        A method which we use to update the display's message.
        It takes one parameter called data.
        :param data: a dictionary containing the data to be displayed
        for key, value in the dictionary, self.message attribute in the display will equal the value
        Then we print the key and value to the user.
        """
        #self.message = data["message"]
        for key, value in data.items():
            self.message = value
            print(f"{key}: {value}")


#display1 = Display(id="Display 1:", car_park=2, message="Welcome to the car park", is_on=True)
#print(display1)