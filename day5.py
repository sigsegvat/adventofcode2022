import re

with open('day5.txt', 'r') as file1:
    lines = list(map(str.strip,file1.readlines()))

stacks=[""]*9

for line in reversed(lines[:8]):
    print(line)
    ind=0
    for i in range(1,len(line),4):
        if line[i].strip():
            stacks[ind]+=line[i]
        ind+=1

print(stacks,sum(map(len,stacks)),list(map(len,stacks)))

for line in lines[10:]:
    crates,froms,tos = [int(n) for n in re.findall(r'\d+', line)]
    print(line)
    for i in range(crates):
        crate = stacks[froms-1][-1]
        print("move ",crate, stacks)
        stacks[froms-1] = stacks[froms-1][:-1]
        stacks[tos-1] += crate
    
    print(stacks, sum(map(len,stacks)),list(map(len,stacks)))

print(list(map(lambda s: s[-1],stacks)))
