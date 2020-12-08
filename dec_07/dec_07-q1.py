import re
file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_07/dec_07.txt", "r")
bags = file.readlines()

bags = [i.split(' ') for i in bags]
sets=[[],[]]
iteration_sets=[[],[]]
null_set=set()
flag=True
shiny_boi=set(['shiny gold'])

for row in range(len(bags)):
    contents=0
    if len(bags[row])==7 : #0 1
        sets[0].append(set([bags[row][0]+' '+bags[row][1]]))    #lägger in väskan som ett set i sets[0]
        sets[1].append(set([]))                                 #eftersom väskan inte innehåller något sparas ett tomt set i sets[1]

    elif len(bags[row])==8 :#0 1 | 5 6
        sets[0].append(set([bags[row][0]+' '+bags[row][1]]))    #lägger in väskan som ett set i sets[0]
        contents=[(bags[row][5]+' '+bags[row][6])]              #samlar ihop alla väskor som väskan innehåller och sparar i variabeln contents
        sets[1].append(set(contents))                           #sparar de underordnade väskorna som ett seet i sets[1]

    elif len(bags[row])==12 :#0 1 | 5 6 | 9 10
        sets[0].append(set([bags[row][0]+' '+bags[row][1]]))    #lägger in väskan som ett set i sets[0]
        contents=[(bags[row][5]+' '+bags[row][6])]              #samlar ihop alla väskor som väskan innehåller och sparar i variabeln contents
        contents= contents+[(bags[row][9]+' '+bags[row][10])]   #-||-
        sets[1].append(set(contents))                           #sparar de underordnade väskorna som ett seet i sets[1]

    elif len(bags[row])==16 : #0 1 | 5 6 | 9 10 | 13 14
        sets[0].append(set([bags[row][0]+' '+bags[row][1]]))    #lägger in väskan som ett set i sets[0]
        contents=[(bags[row][5]+' '+bags[row][6])]              #samlar ihop alla väskor som väskan innehåller och sparar i variabeln contents
        contents= contents+[(bags[row][9]+' '+bags[row][10])]   #-||-
        contents= contents+[(bags[row][13]+' '+bags[row][14])]  #-||-
        sets[1].append(set(contents))                           #sparar de underordnade väskorna som ett seet i sets[1]

    elif len(bags[row])==20 : #0 1 | 5 6 | 9 10 | 13 14 | 17 18
        sets[0].append(set([bags[row][0]+' '+bags[row][1]]))    #lägger in väskan som ett set i sets[0]
        contents=[(bags[row][5]+' '+bags[row][6])]              #samlar ihop alla väskor som väskan innehåller och sparar i variabeln contents
        contents= contents+[(bags[row][9]+' '+bags[row][10])]   #-||-
        contents= contents+[(bags[row][13]+' '+bags[row][14])]  #-||-
        contents= contents+[(bags[row][17]+' '+bags[row][18])]  #-||-
        sets[1].append(set(contents))                           #sparar de underordnade väskorna som ett seet i sets[1]

    else:
        print('uh oh') #bör inte vara längre än 20 ord

# ta in alla och konvertera till sets [KLAR]

#iterera en gång och få ut alla väskor som kan ha en shiny gold i sig
for i in range(len(bags)):
    if shiny_boi.issubset(sets[1][i]):
        iteration_sets[0].append(sets[0][i])



#iterera flera gånger och kolla vilka väskor som kan ha en väska so mhar en shiny gold i sig osv.osv
counter =0
#for i in range(len(iteration_sets[counter])):  #det ska nog vara en while loop
while True:
    iteration_sets.append([])
    if iteration_sets[counter]:
        for i in range(len(iteration_sets[counter])):
            for u in range(len(sets[0])):
                if iteration_sets[counter][i].issubset(sets[1][u]):
                    iteration_sets[(counter+1)].append(sets[0][u])
    else:
        break
    counter+=1


counter_2=0
temp=set()
u=0
for u in range(len(iteration_sets)):
    temp=set()
    for i in range(len(iteration_sets[u])):
        temp=temp.union(iteration_sets[u][i])
    counter_2+=len(temp)    

print(counter_2)


#summera antal sets som har itererats fram