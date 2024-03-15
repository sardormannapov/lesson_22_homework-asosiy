inp = input("Enter magic function: ")
class Magic_Function:
    def __init__(self, magic_replace, magic_string_length, magic_trim, magic_list_slice, inp):
        self.magic_replce = magic_replace
        self.magic_string_length = magic_string_length
        self.magic_trim = magic_trim
        self.magic_list_slice = magic_list_slice
        self.input = inp


    def get_magic_replace(self):
        return f"{self.magic_replce}".replace("E", "e")

    def get_magic_string_length(self):
        return len(f"{self.magic_string_length}")

    def get_magic_trim(self):
        return f"{self.magic_trim}"

    def get_magic_list_slice(self):
        return f"{self.magic_list_slice}"


obj = Magic_Function("AzErty-QwErty", "hello world", "       python is awesome       ", f"{[1, 2, 3, 4, 5]} {(2, 3)}", inp=inp)
if inp == "magic.replace":
    print(obj.get_magic_replace())

elif inp == "magic.str_length":
    print(obj.get_magic_string_length())

elif inp == "magic.trim":
    print(obj.get_magic_trim())

elif inp == "magic.list_slice":
    print(obj.get_magic_list_slice())
