f = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_3/dec_3.txt", "r")
temp = f.readlines()
hill = [i.replace('\n','') for i in temp] 

#Q1
# vert=0
# counter=0
# for hor horn range(len(hill)):
#     vert = vert % 31
#     if hill[hor][vert] == '#':
#         counter += 1
#     vert += 3
# print(counter)


#Q2
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2],]     #[rightstep,downstep]
trees=1
for case in range(len(slopes)):
    counter = 0
    hor=0
    vert=0
    while True:
        vert = vert % 31
        if hill[hor][vert] == '#':
            counter += 1
        vert += slopes[case][0]
        hor += slopes[case][1]
        if hor >= len(hill):
            trees=trees*counter
            break
print(trees)
