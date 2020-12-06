import operator
f = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_02/dec_02.txt", "r")
list = f.readlines()
counter =0

numbers = [i.split(' ')[0] for i in list]
numbers = [i.split('-') for i in numbers]
letters = [i.split(' ')[1] for i in list]
passwords = [i.split(' ')[2] for i in list]
passwords = [i.replace('\n','') for i in passwords] 

for i in range(len(list)):      
    A=bool(letters[i][0]==passwords[i][int(numbers[i][0])-1])
    B=bool(letters[i][0]==passwords[i][int(numbers[i][1])-1])
    xor=bool(A*operator.not_(B)+operator.not_(A)*B)
    if xor:
        counter+=1

print(counter)