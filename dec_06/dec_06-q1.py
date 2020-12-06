file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_06/dec_06.txt", "r")
declaration = file.read()

declaration = declaration.split('\n\n')
declaration = [i.replace("\n", "") for i in declaration]

questions=0

for i in range(len(declaration)):
    questions += len("".join(dict.fromkeys(declaration[i])))
print(questions)