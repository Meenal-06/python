class contact:
    def __init__(self,f_name,l_name,con_no1,con_no2,email,add,category):
        self.f_name=f_name
        self.l_name=l_name
        self.con_no1=con_no1
        self.con_no2=con_no2
        self.email=email
        self.add=add
        self.category=category
    def putdata(self):
        f=open('contact.txt','a')
        f.write(self.f_name+"|"+self.l_name+'|'+self.con_no1+"|"+self.con_no2+'|'+self.email+"|"+self.add+"|"+self.category+"\n")
        f.close()
    def getdata(self):
         f=open('contact.txt','r')
         x=f.read()
         #print(f_name+'  |  '+l_name+'  |  '+con_no1+'  |  '+con_no2+'|'+email+"|"+add+"|"+category+\n")
         #y=x.split()
         print(x)
         print("\n")
         f.close()


f_name=input('Enter your first name: ')
l_name=input('Enter your last name: ')
con_no1=input('Enter your contact number1: ')
con_no2=input('Enter your contact number2: ')
email=input('Enter your email:')
add=input('Enter your address:')
category=input('Enter your category ')
print("\n")
print('First Name| Last Name | Contact Number 1|Contact Number 2|email|Address| category\n')

c1=contact(f_name,l_name,con_no1,con_no2,email,add,category)
c1.putdata()
c1.getdata()
