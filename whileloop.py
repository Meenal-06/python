print('While loop')
y=int(input('Enter any year: '))
if((y%400==0)and (y%4==0)):
    print('year is a leap year')
elif(y%100!=0):
    print('year is not a leap year')
else:
    print('year is not a leap year')
