# %%

# [fill this line]
import figure # figure 파일 import
    
myline = figure.line(10, -1)
width, height = myline.get_length()

try :
    rectangle = figure.area_rectangle(width, height) 
    ellipse = figure.area_ellipse(width, height)
    right_triangle = figure.area_right_triangle(width, height)
    print(rectangle)
    print(ellipse)
    print(right_triangle)
except ValueError :
    print("please input positive number for width and height")