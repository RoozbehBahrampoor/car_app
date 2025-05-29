from validator import car_validator

class Car:
    def __init__(self, name, model, color, production_date, owner):
        self.name = name
        self.model = model
        self.color = color
        self.production_date = production_date
        self.owner = owner

    def save(self):
        print(self.name + " " + self.model + " " + self.color + " " + self.production_date + " " + self.owner + " saved")


        def find_by_model(self):
            print(f"{self.model} Found ")

    def to_tuple(self):
        return (self.name, self.model, self.color, self.production_date, self.owner)

    def validator(self):
        return car_validator(self)
