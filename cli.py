#fuction to add
def add(a1,a2):
	ad=a1+a2
	return(ad)
#fuction to sub
def sub(s1,s2):
	sb=s1-s2
	return(sb)
#fuction to multiplication
def mul(m1,m2):
	mu=m1*m2
	return(mu)
#fuction to division
def div(d1,d2):
	di=d1/d2
	return(di)
#fuction to modulo
def mol(m,mo):
	mod=m%mo
	return(mod)
#to find power
def pow(x1,y1):
        p=x1**y1
        return(p)
print('                           Welcome!! To Meenal Calculator                                          ')
#asking unary or binary
def cal():
        a1=str.lower(input('Which type of operation you want to perform (unary,binary)'))
#asking int or float
        a=str.lower(input('which type of value you  want to insert(int,float) ='))
#check conditon of unary and binary
        if(a=='int'and a1=='binary'):
                v1=int(input('Enter first value'))
                v2=int(input('Enter second value'))
        elif(a=='float' and a1=='binary'):
                v1=float(input('Enter first value'))
                v2=float(input('Enter second value'))
        elif(a=='int'and a1=='unary'):
                v1=int(input('Enter value:'))
        elif(a=='float' and a1=='unary'):
                v1=float(input('Enter value:'))
        else:
                print('Enter valid choice')
                exit()
        #for unary operation
        if(a1=='unary' and a=='int' or a=='float'):
                print('** for square')
                print('*** for cube')
                print('sq for square root')
                print('cu for cube root')
                choice=input('Enter your choice')
                if(choice=='**'):
                        x=v1*v1
                        print('square of',v1,'=',x)
                elif(choice=='***'):
                        x=v1*v1*v1
                        print('Cube of',v1,'=',x)
                elif(choice=='sq'):
                        x=v1**0.5
                        print('square root of',v1,'=',x)
                elif(choice=='cu'):
                        x=v1**(1/3)
                        print('Cube root of',v1,'=',x)
                        
        #for binary operation
        elif(a1=='binary' and a=='int' or a=='float'):
                print('+ for Addition ')
                print('- for Subtraction ')
                print('* for Multipilcation ')
                print('/ for Division ')
                print('% for Modulo ')
                print('^ for power')
                choice=input('Enter your choice')
                if(choice=='+'):
                    x=add(v1,v2)
                    print(v1 ,'+',v2,'=',x)
                elif(choice=='-'):
                    x=sub(v1,v2)
                    print(v1, '-',v2,'=',x)
                elif(choice=='*'):
                    x=mul(v1,v2)
                    print(v1, '*',v2,'=',x)
                elif(choice=='/'):
                    if(v2==0):
                        print('Division by 0 not allowed')
                    else:
                        x=div(v1,v2)
                        print(v1, '/',v2,'=',x)
                elif(choice=='%'):
                        if(v2==0):
                                print('Division by 0 not allowed')
                        else:
                                x=mol(v1,v2)
                                print(v1, '%',v2,'=',x)
                elif(choice=='^'):
                        x=pow(v1,v2)
                        print(v1,'^',v2,'=',x)
                
                else:
                        print('Invalid choice!!!!,Enter valid choice')
        return(x)
k=cal()
#ask user to calculate again
q=str.lower(input('You want to calculate again  (yes/no)'))
if(q=='yes'):
         cal()
elif(q=='no'):
        print('Thankyou!!! Visit Again')
        exit()


