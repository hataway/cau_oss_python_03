from math import pi
from math import sqrt

class line :
    _length = 10
    
    def __init__(self, num):
        self._number = num
    
    def set_length(self,num) :
        self._length = num
        
    def get_length(self) :
        return self._length

def area_square(length) :
    return length*length

def area_circle(length) :
    return length*length*pi

def area_regular_triangle(length) :
    return length*length*sqrt(3)/4