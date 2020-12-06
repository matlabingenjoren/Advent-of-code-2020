import re
file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_05/dec_05.txt", "r")
ticket = file.readlines()

ticket = [i.replace('\n','') for i in ticket]
ticket = [i.replace('B','1') for i in ticket]
ticket = [i.replace('F','0') for i in ticket]
ticket = [i.replace('R','1') for i in ticket]
ticket = [i.replace('L','0') for i in ticket]

row=0
col=0
seats=[]
mySeat=0

for i in range(len(ticket)):
    row=int(ticket[i][:-3],2)
    col=int(ticket[i][-3:],2)
    seatID=row*8+col
    seats.append(seatID)

seats.sort()

for i in range(len(seats)-1):
    if seats[i+1]-seats[i] > 1:
        mySeat=(seats[i+1]+seats[i])/2

print(mySeat)

if re.search('[69]',str(mySeat)):
    print('Nice.')