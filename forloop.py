#for loop
#n=10
#for i in range(n):
#for i in range(1,n+1):
n=int(input('Enter a number to print the table:'))
count=1
for i in range(n,n*10+1,n):
    #print(n,"*",i//n,"=",i)
    print("{}*{}={}".format(n,count,i))
    count=count+1

