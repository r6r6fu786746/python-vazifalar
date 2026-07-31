# import time

# class Car:
#     """Represent a car with a color and model."""

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def get_info(self, location):
#         caption = "Car info:"
#         return f"{caption} {self.color} {self.model} {location}da yurmoqda"


# car = Car("Blue", "BMW")
# print(car.get_info('Tashkent'))

# Task, TODO file yarat, ichida malumot olib ketgan odam malumot, olib ketish vaqti, olib ketilgan sanasi borilsin

from datetime import datetime

now = datetime.now()

vaqt = now.strftime("%d.%m.%Y %H:%M:%S")

data = open('book_data.xlsx', 'w')



class Book:

    def __init__(self, name, author, limit):
        self.name = name
        self.author = author
        self.limit = limit
        self.status = True

    def borrow(self):
        if self.status:
            self.status = False
            data.write(f"{vaqt} vaqtda [Ismi: {self.name}, Author: {self.author}, Limit: {self.limit} kungacha] kitobi olindi")
            return f"{self.name}, {self.author} olindi"

        else:
            return f"{self.name} kitobi mavjud emas yoki qarzga olinga"

    def qaytar(self):
        if not self.status:
            self.status = True
            data.write(f"{vaqt} vaqtda [Ismi: {self.name}, Author: {self.author}, Limit: {self.limit} kungacha] kitobi qaytarildi")
            return  f"{self.name} kitobi qaaytarildi"
        else:
            return f"Kitob sizdaa yuq"

Atomic = Book('Atomic', "James", '10')
print(Atomic.borrow())

data.close()

