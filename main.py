class species:
    def __init__(self , name , age) :
        self.name=name 
        self.age=age
    def sing (self, song ):
        return f"{self.name } sings {song}"
    def dance (self):
        return f"{self.name } is now dancing "
object1 = species("Cuckoo",14)        
object2 = species("Parrot",12)
    
print (f"{object1.name} is {object1.age} years old")
print (f"{object2.name} is {object2.age} years old")

print(object1.sing("happy"))
print(object1.dance())
print(object2.sing("sad"))
print(object2.dance())

