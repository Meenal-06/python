count=1
def pl():
    global count
    count+=1
def mi():
    global count
    count-=1
print('Count=',count)
pl()
pl()
mi()
mi()
print('count =',count)
