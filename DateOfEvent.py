from msilib.schema import Class
from multiprocessing import Event


class Date_of_Event:
    def __init__(self, date):
        self.date = date
        self.date_array = date.split('/')
        self.date_array_2 = [0]*3
        i = 0
        for i in range(0,3):
            self.date_array_2[i] = float(self.date_array[i])
        print(self.date_array_2)