inp = input("enter foods: ")
class Person:
    def __init__(self, name, foods_loves, foods_hate, inp):
        self.name = name
        self.foods_loves = foods_loves
        self.foods_hate = foods_hate
        self.inp = inp

    def food_love(self):
        return f"{self.name} eats the {self.foods_loves} and loves it!"

    def food_hate(self):
        return f"{self.name} eats the {self.foods_hate} and hates it!"


obj = Person("Sam", "ice cream", "carrots", inp=inp)
if inp == "ice cream":
    print(obj.food_love())

elif inp == "carrots":
    print(obj.food_hate())

else:
    print(f"Sam eats {inp}")
