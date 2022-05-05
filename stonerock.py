#stone paper scissor
import random
print('stone=1')
print('Paper=2')
print('scissor=3')
n=int(input('Enter a number how many time you want play:'))
for i in range(n):
    a=int(input('Select any number user 1:'))
    b=random.randint(1,3)
    print('Computer select: ',b)
    # b=int(input('select any number user2: '))
    if(a==b):
         print("Game Draw")
    elif((a==1 and b==2)or(a==2 and b==1 )or(a==3 and b==2 )) :
        print('Congratulation user 1 you win')
        print('opps!!! user2 lost')
    elif((a==1 and b==2)or(a==2 and b==3 )or( a==3 and b==1) ): 
        print('Congratulation user 2 you win')
        print('Ooops!!!,user 1 lost')
    else:
        print('Invalid choice')
