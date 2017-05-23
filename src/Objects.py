'''
Created on May 23, 2017
Python Object Oriented Programming Fundamentals
@author: makaidaimyo
'''
class cEmployee:
    'Base class Employee' #Documentation

    #Class variables
    var1 = 0
    var2 = 10

    #Constructor
    def __init__(self):
        self.first_name = 'n/a'
        self.last_name = 'n/a'
        self.uid = 'n/a'
    #Destructor
    def __del__(self):
        print("The end of", self.__class__.__doc__)
        
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

def main():
    emp1 = cEmployee()
    
    print('Default values =>', 'User Id: ', emp1.get_uid(), 'Employee Name: ', emp1.get_full_name())
    emp1.set_first_name('Fernando')
    emp1.set_last_name('Dantas')
    emp1.set_uid('278')
    print('Changed values =>', 'User Id: ', emp1.get_uid(), 'Employee Name: ', emp1.get_full_name())
  
    

main()