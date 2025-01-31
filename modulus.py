import math
a=int(input())
b=int(input())
m=int(input())
def powers(a,b):
    return pow(a,b)
    
def modulus(a,b,m):
     return ((a**b) % m )
     
print (powers(a,b))
print (modulus(a,b,m))