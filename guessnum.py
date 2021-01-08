import random as ran

def getdata(): 
    return list( int(x) for x in input("Enter Your Guess for Four Digit Number : "))


#comp=list(ran.randint(0,9) for x in range(4))
comp=[4,1,3,2]
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
    if 'P' in flag: continue
    print(*user)    
    print(*flag)
    for x in flag:
        if all(ele == 'C' for ele in flag):
            loop=False
            break
    user =getdata()
    print(flag)
    print(dup)
    dup=comp.copy()
    print(dup)
       
print("congratulation You Found the Number ")             
print(comp)
print(user)





