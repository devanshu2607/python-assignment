##41.	Define a class for a Rectangle that calculates the area and perimeter.
class rectangle:
    def __init__(self,length,width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width
    def perimeter (self):
        
        return 2*(self.length + self.width)
  #example usage   
rectangle = rectangle(9,7)
print("area:", rectangle.area())
print("perimeter:",rectangle.perimeter())


