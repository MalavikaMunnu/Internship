class Laptop:
    def __init__(self,brand,ram,rom):
        # print(self)
        self.Brand=brand
        self.RAM=ram
        self.ROM=rom
    def __str__(self):
        return self.Brand
    def display_ram(self):
        print("RAM value of",self.Brand,"is",self.RAM)
    def display_rom(self):
        print("ROM value of",self.Brand,"is",self.ROM)
    def __del__(self):
        print("Object destructed!!",self)
ob=Laptop("HP","8GB","512GB")
# ob.display_ram()
# ob.display_rom()

oc=Laptop("DELL","8GB","512GB")
# oc.display_ram()
# oc.display_rom()

print(ob)
print(oc)