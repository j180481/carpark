class Display:
    def __init__(self, identity, car_park, message="", is_on=False):
        self.identity = identity
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f'{self.identity} {self.message}'

    def update(self, data):
        #self.message = data["message"]
        for key, value in data.items():
            self.message = value
            print(f"{key}: {value}")


#display1 = Display(id="Display 1:", car_park=2, message="Welcome to the car park", is_on=True)
#print(display1)