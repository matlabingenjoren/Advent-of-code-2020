file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_06/dec_06.txt", "r")
declaration = file.read()

declaration = declaration.split('\n\n')
declaration = [i.split('\n') for i in declaration]

questions=0

for i in range(len(declaration)):
    set1=set(declaration[i][0])
    for u in range(1,len(declaration[i])):
        set2=set(declaration[i][u])
        set1=set1.intersection(set2)
    questions+=len(set1)
    
print(questions) 