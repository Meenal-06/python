'''list1=[12,223,34567,23456,456,234,2345]
list_even=[]
print(list1)
print(list_even)
for i in list1:
    if i %2==0:
        list_even.append(i)
print(list_even)
'''
'''def even(n):
    return n%2==0

list1=[12,223,34567,23456,456,234,2345]
list_even=list(filter(even,list1))
print(list1,list_even)
'''
from functools import reduce
list1=[12,223,34567,23456,456,234,2345]
print(list1)
list_even=list(filter(lambda x:x%2==0,list1))
print("Even list=",list_even)
list_even2=list(map(lambda x: x*2,list_even))
print("Even list *2=",list_even2)
list_odd=list(filter(lambda x:x%2!=0,list1))
print("Odd list=",list_odd)
sum1=reduce(lambda x,y:x+y,list_even2)
print(sum1)
