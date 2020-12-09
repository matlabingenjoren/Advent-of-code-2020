file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_09/dec_09.txt", "r")
input = file.readlines()
input = [i.replace('\n','') for i in input]
for i in range(0, len(input)): 
    input[i] = int(input[i])

trail=25

for i in range(trail,len(input)):
    flag_q1=False
    lista=[]
    for u in range(1,(trail+1)):
        if lista:
            for x in range(len(lista)):
                if input[i]-input[i-u]==lista[x]:
                    flag_q1=True

        lista.append(input[i-u])                
    if not flag_q1:
        wrong=i
        break

print('Q1:'+str(input[i]))

start=0
flag_q2=True
smallest=float('inf')
largest=0
while flag_q2:
    smallest=float('inf')
    largest=0
    summa=0
    for y in range(start,(wrong-1)):
        if input[y]<smallest:
            smallest=input[y]
        if input[y-1]>largest:
            largest=input[y-1]   
        if summa==input[i]:
            flag_q2=False
            break   
        if summa>input[i]:
            break

        summa+=input[y]
    start+=1

print('Q2:'+str(smallest+largest))

