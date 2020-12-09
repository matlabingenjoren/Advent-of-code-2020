file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_08/dec_08.txt", "r")
inst = file.readlines()
inst = [i.split(' ') for i in inst]
for i in range(0, len(inst)): 
    inst[i][1] = int(inst[i][1])

acc=0
visited=set()
x=0
temp=0

#BRUTE FORCE OF HELL
#fråga inte. det funkar
jumpsnopes=[]
for i in range(len(inst)):
    if inst[i][0]=='jmp':
        jumpsnopes.append(i)
    if inst[i][0]=='nop':
        jumpsnopes.append(i)

for j in range(len(jumpsnopes)):

    file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_08/dec_08.txt", "r")
    inst = file.readlines()
    inst = [i.replace('\n','') for i in inst]
    inst = [i.split(' ') for i in inst]
    
    for i in range(0, len(inst)): 
        inst[i][1] = int(inst[i][1])
        
    acc=0
    visited=set()
    x=0
    temp=0
    
    #swapping nop and jmp
    if inst[jumpsnopes[j]][0]=='jmp':
        inst[jumpsnopes[j]][0]='nop'
    else:   
        inst[jumpsnopes[j]][0]='jmp'

    while True:
        x+=temp
        if  x==len(inst):
            print(acc)
            break
        temp=0
        if len(visited)==len(visited.union({x})):
            break
        if inst[x][0] == 'nop':
            temp+=1
            visited=visited.union({x})
            continue
        if inst[x][0] == 'acc':
            acc+=inst[x][1]
            temp+=1
            visited=visited.union({x})
            continue
        if inst[x][0] == 'jmp':
            temp+=inst[x][1]
            visited=visited.union({x})
        