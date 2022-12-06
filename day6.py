with open('day6.txt', 'r') as file1:
    signal = file1.readline().strip()

recent = []
processed = 0

for s in signal:
    recent=  [s] + recent
    processed +=1
    if len(recent) > 14:
        del recent[-1]
    if len(recent) == 14:
        if(len(set(recent))==14):
            print("found",processed, recent)
            break
        else:
            print("xxxxx",processed, recent)
    
