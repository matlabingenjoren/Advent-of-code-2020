
f = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_3/dec_3.txt", "r")
list = f.readlines()

slope = [i.replace('\n','') for i in list] 

#Q1
# u=0
# counter=0
# for i in range(len(slope)):
#     u = u % 31
#     if slope[i][u] == '#':
#         counter += 1
#     u += 3
# print(counter)


#Q2
case = [[1,1],[3,1],[5,1],[7,1],[1,2],]     #[rightstep,downstep]
trees=1
for a in range(len(case)):
    counter = 0
    i=0
    u=0
    while True:
        u = u % 31
        if slope[i][u] == '#':
            counter += 1
        u += case[a][0]
        i += case[a][1]
        if i >= len(slope):
            trees=trees*counter
            break
print(trees)
