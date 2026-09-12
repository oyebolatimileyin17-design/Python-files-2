class Animal:
   
   def __init__(self, name):
       self.name = name

   def speak(self):
       print(f"{self.name} makes a sound")

class Dog(Animal):
   
   def speak(self):
         print(f"{self.name} says Woof!")
dog1  = Dog("Rex")
dog1.speak()

class Cat(Animal):
   
   def speak(self):
       print(f"{self.name} says meow!")
cat1 = Cat("Whiskers")
cat1.speak()
