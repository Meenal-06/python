print("This script is intended to swap the values of two data variable using third temprory variable ")
a=(input('Enter first number: '))
b=(input('Enter second number: '))
print("value before swapping ",)
print("a=",a)
print("b=",b)
'''c=a
a=b
b=c'''
a=int(a)
b=int(b)
a=a+b
b=a-b
a=a-b

print("value after swaping ")
print("a="+str(a))
print("b="+str(b))

