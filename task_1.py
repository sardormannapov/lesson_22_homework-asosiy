inp = input("Enter two attributes: ")
class Book:
    def __init__(self, title, author, inp):
        self.title = title
        self.author = author
        self.inp = inp

    def titlee(self):
        return f"{self.title}"

    def authorr(self):
        return f"{self.author}"

    def get_titlee(self):
        return f"Title: {self.title}"

    def get_authorr(self):
        return f"Author: {self.author}"



obj = Book("Harry Potter", "J.K. Rowling", inp=inp)
if inp == "title":
    print(obj.titlee())

elif inp == "author":
    print(obj.authorr())

elif inp == "get_title":
    print(obj.get_titlee())

elif inp == "get_author":
    print(obj.get_authorr())

