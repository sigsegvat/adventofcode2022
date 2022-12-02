file1 = open('day1.txt', 'r')
Lines = file1.readlines()

top=[0,0,0]
sum = 0
for line in Lines:

    if line!="\n":
        current = int(line)
        sum+=current
    else:
        if(sum>top[0]):
            top[0]=sum
        elif(sum>top[1]):
            top[1]=sum
        elif(sum>top[2]):
            top[2]=sum
        top.sort()
        sum=0

print("tops: ", top)
print("tops: ", top[0]+top[1]+top[2])