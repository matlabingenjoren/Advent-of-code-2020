f = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_03/dec_03.txt", "r")
temp = f.readlines()
hill = [i.replace('\n','') for i in temp] 

vert=0
counter=0

for hor in range(len(hill)):
    vert = vert % 31
    if hill[hor][vert] == '#':
        counter += 1
    vert += 3
print(counter)