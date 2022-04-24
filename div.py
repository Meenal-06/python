#divisor
a=int(input('how many time you want to calculate diviosr of number'))
for i in range(1,a+1):
      n=int(input('\nEnter a number'))
      for i in range(1,n+1):
            if(n%i==0):
                  print(i,end=' ')
else:
      exit()

