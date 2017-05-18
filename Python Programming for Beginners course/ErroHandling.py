class calc:
    def sum(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mult(a,b):
        return a*b
    def div(a,b):
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

import Test as T

try:
    x=1/0
except Exception as e:
    print("general error catch: ", e)

print("code continues")

try:
    a = 10
    b = 11
    assert (a>=b), "B is greater than A"
except AssertionError as e:
    print(e)
