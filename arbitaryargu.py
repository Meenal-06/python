def avg(*value):
    x=0
    for i in value:
        x+=i
    return x/len(value)
w=avg(2,3,4,5,6)
print(w)
r=avg(2,5,6)
print(r)
