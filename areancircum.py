
print('This Program calculate area and circumference of circle ')
def area(n):
    x=3.14*n*n
    return (x)
def circum(c):
    y=2*3.14*c
    return(y)
q=int(input('How many time you want to calculate area and circumference of circle:'))
for i in range(q,0,-1):
    a=int(input('Enter radius of circle'))
    ar=area(a)
    cr=circum(a)
    x=round(ar,1)
    print('Area of circle: ',x)
    x=round(ar,4)
    print('Circumference of circle: ',x)
