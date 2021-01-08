import random as ran

def getdata(): 
    return list( int(x) for x in input("Enter Your Guess for Four Digit Number : "))


comp=list(ran.randint(0,9) for x in range(4))
print(comp)
dup=comp.copy()
user=getdata()
flag=['X','X','X','X']
loop=True    
while loop:  
    i=0
    while i<4:
        if comp[i] == user[i]:
            flag[i]='C'
            #del comp[i]          
        elif user[i] in comp :
            flag[i]='P'
        else:
            flag[i]='X'
        i+=1
    print(*user)    
    print(*flag)
    for x in flag:
        if x=='C':
            loop=False
    user =getdata()
       
print("congratulation You Found the Number ")             







