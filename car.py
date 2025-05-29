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


#شی سازی
car1 = Car("benz" , "gclass" , "red" , "2023" , "ali")
car2 = Car("benz" , "cls" , "blue" , "2022" , "reza")


car1.save()
car2.save()



