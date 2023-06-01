from math import pi
from math import sqrt

class line :
    _width = 10 
    _height = 20
    
    def __init__(self, width, height):
        self._width = width # 생성자 초기 width 값
        self._height = height # 생성자 초기 height 값
    
    def set_length(self, width, height) : # setter
        self._width = width 
        self._height = height 
        
    def get_length(self) : # getter
        return self._width, self._height

def area_rectangle(width, height) : # rectangle 함수
    if width <= 0 or height <= 0 : raise ValueError
    return width * height

def area_ellipse(width, height) : # ellipse 함수
    if width <= 0 or height <= 0 : raise ValueError
    return width * height * pi

def area_right_triangle(width, height) : # right_triangle 함수
    if width <= 0 or height <= 0 : raise ValueError
    return width * height / 2