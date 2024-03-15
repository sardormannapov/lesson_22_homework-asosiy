inp = input("enter salary or work_hours: ")
class Mini_challenge:
    def __init__(self, salary, work_hours, inp=inp):
        self.salary = salary
        self.work_hours = work_hours
        self.input = inp

    def salar(self):
        return f"{self.salary}"

    def workhours(self):
        return f"{self.work_hours}"




obj = Mini_challenge("25000", "5", inp=inp)
if inp == "prog.salary":
    print(obj.salar())

elif inp == "prog.work_hours":
    print(obj.workhours())
    
