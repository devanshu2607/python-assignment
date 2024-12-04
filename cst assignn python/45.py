##45.	Create an abstract class Animal with subclasses for Dog and Cat.
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class dog(animal):
    def make_sound(self):
        return "woof!"

    def move(self):
        return "the dog runs."


class cat(animal):
    def make_sound(self):
        return 'meow!'
    
    def move(self):
        return "the dog runs."

dog=dog()
cat=cat()

print(f"dog: {dog.make_sound()}, {dog.move()}")
print(f"dog: {cat.make_sound()}, {cat.move()}")
  