#if else statement user defined
a=int(input('Enter a number'))
#a=int(a)
c=a%2
print(c)
if(a==0):
    print("Number is neither odd nor even")
elif(a%2==0):
    print('Number is even')
else:
    print('Number is odd')
