#find maximum in 3 numbers
a= int(input('Enter First number'))
b= int(input('Enter Second number'))
c= int(input('Enter Third number'))
if(a==b and b==c and c==a):
       print('All values are equal')
elif(a==b and c<a ):
       print(a, 'and', b, 'is equal and is greater than', c )
elif(b==c and a<b):
       print(b,'and' ,c, 'is equal and is greater than ',a)
elif(a==c and b<a):
       print(a, 'and', c,' is equal and is greater than',b)
elif(a==b and c>a ):
       print(a, 'and', b, 'is equal and is less than', c)
elif(b==c and a>b):
       print(b,'and' ,c, 'is equal and is less than',a)
elif(a==c and b>a):
       print(a, 'and', c,' is equal and is less than',b)
elif(a>b and a>c):
       print(a,'is greater than ',b,' and', c)
elif(b>a and b>c):
    print(b,'is greater than',a,'and',c)
else:
    print (c,'is greater than',a,'and',b)
