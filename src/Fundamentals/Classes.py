class calc:
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b


Calc1 = calc

a = 1#float(input("First number"))
b = 2#float(input("Second number"))
#print(Calc1.sum(a,b))

import statistics as std

from statistics import mean as md

exList = [5,3,2,9,7,4,3,1,8,9,9]
print(md(exList))
print(std.median(exList))
print(std.mode(exList))
print(std.stdev(exList))
print(std.variance(exList))

#import Test as T

#T.func1()
    
    
