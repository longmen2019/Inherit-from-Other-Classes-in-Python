class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#dunder str changes what get printed. 
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} barks:{sound}"

#Create a Child Class Named GoldenRetriever Class

#This Child Class inherits from the Dog Class
class GoldenRetriever(Dog):
    def speak(self, sound = "Woof Woof"):
# Access the parent class from inside a method of a child class using super():        
        return super().speak(sound)
    
justine = GoldenRetriever("phillip", 34)
print(justine.speak())
