class Country:
    def __init__(self, country, population, area):
        self.is_big = ""
        self.country = country
        self.population = population
        self.area = area

        if self.population > 250000 and self.area > 3000:
            self.is_big = True

        self.is_big = False


    def compare(self, other):
        if self.population < other.population:
            return f"{self.country} has a larger population denastiy than {other.country}"


obj = Country("Australia", 23545500, 7692024)
obj1 = Country("Andorra", 76098, 468)
print(obj.is_big)
print(obj1.is_big)
print(obj1.compare(obj))
