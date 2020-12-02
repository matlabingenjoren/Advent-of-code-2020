import operator
f = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_2.txt", "r")
list = f.readlines()
counter =0

# Question 1
# numbers = [i.split(' ')[0] for i in list]
# numbers = [i.split('-') for i in numbers]
# letters = [i.split(' ')[1] for i in list]
# passwords = [i.split(' ')[2] for i in list]
# passwords = [i.replace('\n','') for i in passwords] 


# for i in range(len(list)):
#     x=passwords[i].count(letters[i][0])
#     if int(numbers[i][0])<=x<=int(numbers[i][1]):
#         counter+=1


#Question 2
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