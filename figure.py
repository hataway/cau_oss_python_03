from math import pi
from math import sqrt

class line :
    _length = 10 
    
    def __init__(self, num):
        self._number = num # 생성자 초기 length 값
    
    def set_length(self,num) :
        self._length = num # setter
        
    def get_length(self) :
        return self._length # getter

def area_square(length) :
    return length*length # 정사각형 넓이 계산

def area_circle(length) :
    return length*length*pi # 원 넓이 계산, pi = 3.14 ....

def area_regular_triangle(length) :
    return length*length*sqrt(3)/4 # 삼각형 넓이 계산, sqrt = 루트 