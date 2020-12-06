import re
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
        if not (person.byr and len(person.byr)==4 and 1920<=int(person.byr)<=2002):
            continue
        if not (person.iyr and len(person.iyr)==4 and 2010<=int(person.iyr)<=2020):
            continue
        if not (person.eyr and len(person.eyr)==4 and 2020<=int(person.eyr)<=2030):
            continue
        if person.hgt:
            if not (person.hgt[-2:]=='cm' or person.hgt[-2:]=='in'):
                continue
            if person.hgt[-2:]=='cm':
                if not 150<=int(person.hgt[:-2])<=193:
                    continue
            if person.hgt[-2:]=='in':
                if not 59<=int(person.hgt[:-2])<=76:
                    continue
        else:
            continue
        if not (person.hcl and re.search('^#+[a-f0-9]{6}$',person.hcl)):
            continue
        if not (person.ecl and re.search('^(amb|blu|brn|gry|grn|hzl|oth)$',person.ecl)):
            continue
        if not (person.pid and re.search('^[0-9]{9}$',person.pid)):
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