##43.	Implement inheritance by creating a Circle class that inherits from a Shape class.

class shape :
    def __init__(self , color="black"):
        self.color=color
    
    def display_color(self):
        print(f"the color of the shape is {self.color}")

import math


class circle(shape):
    def __init__(self, radius ,color="black"):
        super().__init__(color)
        self.radius=radius

    def area(self):
        return math.pi *( self.radius ** 2)
    
    def perimeter(self):
        return 2* math.pi * self.radius 

    def display_info(self):
        print(f"circle with radius: {self.radius}")
        print(f"circle : {circle.color}")
        print(f"circle area :{circle.area():}")
        print(f"circle perimeter : {circle.perimeter():}")

circle=circle(radius=5,color="blue")

circle.display_info()
