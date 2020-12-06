file = open("C:/Users/Oskar/Documents/Python/24 days of code/dec_04/dec_04.txt", "r")
temp = file.read()

passports = []
persons = []

class Person:
    byr=False
    iyr=False
    eyr=False
    hgt=False
    hcl=False
    ecl=False
    pid=False
    cid=False

def validate(persons):
    counter = 0
    for person in persons:
        if not person.byr:
            continue
        if not person.iyr:
            continue
        if not person.eyr:
            continue
        if not person.hgt:
            continue
        if not person.hcl:
            continue
        if not person.ecl:
            continue
        if not person.pid:
            continue
        # if not person.cid:
        #     continue
        counter += 1
    return counter  
                   

person=Person()
passports = temp.split('\n\n')



for passport in passports:
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    for elmnt in passport:
        elmnt= elmnt.split(":")
        if elmnt[0] == "byr":
            person.byr = elmnt[1]
        if elmnt[0] == "iyr":
            person.iyr = elmnt[1]
        if elmnt[0] == "eyr":
            person.eyr = elmnt[1]
        if elmnt[0] == "hgt":
            person.hgt = elmnt[1] 
        if elmnt[0] == "hcl":
            person.hcl = elmnt[1] 
        if elmnt[0] == "ecl":
            person.ecl = elmnt[1]
        if elmnt[0] == "pid":
            person.pid = elmnt[1]  
        if elmnt[0] == "cid":
            person.cid = elmnt[1] 
    persons.append(person)
    person = Person()

counter = validate(persons)
print(counter)