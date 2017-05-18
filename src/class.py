class cPerson:
    'Base class Person' #Documentation

    #Class variables
    var1 = 0
    var2 = 10

    #Constructor
    def __init__(self):
        self.a = 1
        self.b = 2
    def __del__(self):
        print("The end of", self.__class__.__doc__)

def main():
    cla = cPerson()
    print(cla.a)

    print(cla.var1, cla.var2)
    cla.var1 = 2
    cla.var2 = 30
    print(cla.var1, cla.var2)
    del cla

main()
