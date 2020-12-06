file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_05/dec_05.txt", "r")
ticket = file.readlines()

ticket = [i.replace('\n','') for i in ticket]
ticket = [i.replace('B','1') for i in ticket]
ticket = [i.replace('F','0') for i in ticket]
ticket = [i.replace('R','1') for i in ticket]
ticket = [i.replace('L','0') for i in ticket]

row=0
col=0
maxSeat=0

for i in range(len(ticket)):
    row=int(ticket[i][:-3],2)
    col=int(ticket[i][-3:],2)

    if row*8+col > maxSeat:
        maxSeat = row*8+col

print(maxSeat)
