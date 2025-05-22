import re
from datetime import datetime

def car_validator(car):
    errors = []

    if not (type(car[0]) == int and car[0]>0):
        errors.append('Car ID must be an integer > 0')

    if not (type(car[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", car[1])):
        errors.append('Car Name is Invalid')

    if not (type(car[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", car[2])):
        errors.append('Car Model is Invalid')

    if not (type(car[3]) == int and car[3]>0):
        errors.append('Color is Invalid')

    if not (type(car[4]) == int and car[4]>0):
        errors.append('production_date is Invalid')

    if not (type(car[5]) == int and car[5]>0):
        errors.append('owner is Invalid')

    return errors


