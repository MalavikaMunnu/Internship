# --- Access Specifiers ---


# >>--- Protected ---<<
class Main:
    _name="main"
    def main_meth(self):
        print(self._name)
class Sub(Main):
    def fun(self):
        print(super._name)
        super().main_meth()
os=Sub()
print(os._name)
os.main_meth()




# >>--- Private ---<<
# class Main:
#     __name="main" 
#     def main_meth(self):
#         print(self.__name)
# ob=Main()
# ob.main_meth()