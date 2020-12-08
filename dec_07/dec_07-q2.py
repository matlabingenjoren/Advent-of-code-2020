# 1 väska innehåller 4 väskor(max)

#    0         1                        5      6               9      10                13     14              17    18
# 'dotted chartreuse' bags contain 5 'light black' bags, 3 'shiny turquoise' bags, 5 'drab lavender' bags, 3 'shiny silver' bags.


# 1 väska innehåller 3 väskor
#      0      1                        5     6               9       10                 13    14
# 'striped salmon' bags contain 3 'dotted silver' bags, 1 'shiny turquoise' bag, 3 'mirrored tan' bags.


# 1 väska innehåller 2 väskor
#      0    1                      5     6              9    10
# 'muted yellow' bags contain 2 'shiny gold' bags, 9 'faded blue' bags.


# 1 väskor innehåller 1 väska
#     0      1                      5    6
# 'bright white' bags contain 1 'shiny gold' bag.


# 1 väska innehåller 0 väskor
#     0     1
# 'dotted black' bags contain no other bags.
a=[[{'light red'}, {'dark orange'}, {'light red'}, {'dark orange'}, {'dark orangutang'}],[{'sdfg red'}, {'dfds orange'}, {'lfdst red'}, {'dajh orange'}, {'hrk orangutang'}]]
counter=0
temp=set()
u=0
for u in range(len(a)):
    temp=set()
    for i in range(len(a[u])):
        temp=temp.union(a[u][i])
    counter+=len(temp)    

print(counter)
