'''
Created on May 23, 2017
Python Object Oriented Programming Fundamentals
@author: makaidaimyo
'''

class cEmployee:
    'Base class Employee' #Documentation

    #Class variables
    __var1 = 0
    var2 = 10

    #Constructor
    def __init__(self, first_name, last_name, uid, a):
        self.first_name = first_name
        self.last_name = last_name
        self.uid = uid
        self.__a = a
        self.__var1 = 24
    #Destructor
    def __del__(self):
        print("The end of", self.__doc__)
        print("Employee.__dict__:", self.__dict__)
        
    def print_var1(self):
        print(self.__var1)
    
    #Gets
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    def get_uid(self):
        return self.uid
    #Sets
    def set_first_name(self, first_name):
        self.first_name  = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_uid(self, uid):
        self.uid = uid
        
    #Show
    def show_employee_info(self):
        print('User Id: ', self.uid, 'Employee Name: ', self.first_name, self.last_name)

def main():
    emp1 = cEmployee('Adriana','Dantas', '123', '23ab')
    print('First values =>')
    emp1.show_employee_info()
    emp1.__var12 = 3
    print(emp1.__var12)
    emp1.__var12 = 6
    print(emp1.__var12)
    emp1.print_var1()
    emp1.set_first_name('Fernando')
    emp1.set_last_name('Dantas')
    emp1.set_uid('278')
    print('Changed values =>')
    emp1.show_employee_info()
    
    del emp1
    
    print('End of the script')

main()