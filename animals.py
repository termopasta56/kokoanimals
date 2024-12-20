class Animals:
    height = 170
    age = 200
    satiety = 170
    
class Capybara(Animals):
    age = 8
    
class Hamster(Capybara):
    height = 20
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
        
nick = Hamster()