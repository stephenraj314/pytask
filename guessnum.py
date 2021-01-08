import random as ran

def getdata(): 
    return list( int(x) for x in input("Enter Your Guess for Four Digit Number : "))
j=0
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
            dup[i]='X'         
        elif user[i] in dup :
            flag[i]='P'
        else:
            flag[i]='X'
        i+=1
    if 'P' in flag:
        if j>0:
            j=0
            pass
        else:
            j+=1
            continue        
    print(*user)    
    print(*flag)
    for x in flag:
        if all(ele == 'C' for ele in flag):
            loop=False
            break
    else:
        user =getdata()
        dup=comp.copy()
       
print("!!!Winner Winner Chicken Dinner!!! \n You Found the Number")             
print(*user)





