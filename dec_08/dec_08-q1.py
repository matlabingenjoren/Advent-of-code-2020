file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_08/dec_08.txt", "r")
inst = file.readlines()
inst = [i.split(' ') for i in inst]
for i in range(0, len(inst)): 
    inst[i][1] = int(inst[i][1])

acc=0
visited=set()
x=0
temp=0

while True:
    x+=temp
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


print(acc)