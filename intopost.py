
prio={'+':1,'-':1,'*':2,'/':2,'^':3}
def dif(infix):
    global top
    num=[]
    for i in exp:
        if(i.isdigit()):
            num.append(i)
        elif(i=='('):
            opr.append(i)
            top=top+1
        elif(i==')'):
            while(opr[top]!='('):
                num.append(opr.pop())
                top=top-1
            opr.pop()
            top=top-1
        else:
            if(top==-1):
                opr.append(i)
                top=top+1
            elif(opr[top]=='('):
                opr.append(i)
                top=top+1
            elif(prio.get(opr[top])>=prio.get(i)):
                num.append(opr.pop())
                top=top-1
                if(top>=0):
                    while(prio.get(opr[top])==prio.get(i)):
                        num.append(opr.pop())
                        top=top-1
                        if(top<0):
                            break
                opr.append(i)
                top=top+1
            elif(prio.get(opr[top])<prio.get(i)):
                    opr.append(i)
                    top=top+1
        while(top!=-1):
                num.append(opr.pop())
                top=top-1
        return num
#main
operator=['+','-','*','%','/']
numeral=['1','2','3','4','5','6','7','8','9','0']
exp=[]
in_ex=input('Enter the value: ')
print('input=',in_ex)
operand=""
for i in in_ex:
    if i in numeral:
        operand=operand+i
    elif i in operator:
        exp.append(operand)
        exp.append(i)
        operand=""
    else:
        print('Invalid chracter')
        break
exp.append(operand)
#infix=list(exp)
print('input expression (in list)=',exp)
opr=[]
top=-1
postfix=dif(exp)
print("Postfix expression",postfix)
'''
in_ex=input('Enter the value: ')
x=eval(in_ex)
print('Evalution of expression=',x)
'''

            
            


            

    
    
