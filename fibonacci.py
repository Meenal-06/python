print('Program to Print Fibonacci Serier')
n=int(input('Enter a number: '))
a=0
b=1
f=0
print(a)
while(b<=n):
    f=a+b
    a=b
    b=f
    print(a)
