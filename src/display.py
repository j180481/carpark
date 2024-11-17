class Display:
    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f'{self.id} {self.message}'

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")


#display1 = Display(id="Display 1:", car_park=2, message="Welcome to the car park", is_on=True)
#print(display1)