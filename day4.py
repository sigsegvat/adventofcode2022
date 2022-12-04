import re

with open('day4.txt', 'r') as file1:
    lines = list(map(str.strip,file1.readlines()))

contains=0
overlap=0
for line in lines:
    (a1,b1,a2,b2) = list(map(int,re.split(r"[-,]",line)))
    first = range(a1,b1+1)
    second = range(a2,b2+1)
    if(all(x in first for x in second) or all(x in second for x in first)):
        contains +=1
    if(any(x in first for x in second) or any(x in second for x in first)):
        overlap +=1

print(contains, overlap)