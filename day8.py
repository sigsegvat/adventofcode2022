

class Forerst:
    def __init__(self,trees) -> None:
        self.trees=trees
        rows = len(trees)
        cols = len(trees[0])
        self.visible = [[False for j in range(rows)] for i in range(cols)]
        self.clear_edge()
        self.rows()
    
    def clear_edge(self):
        for r,row in enumerate(self.visible):
            for c,val in enumerate(row):
                if r == 0 or c == 0 or c==len(row)-1 or r == len(self.visible)-1:
                    self.visible[r][c] = True
    
    def rows(self):
        for row in range(0,len(self.trees)):
            maxheight = 0
            for col in range(0,len(self.trees[row])):
                if int(self.trees[row][col]) > maxheight:
                    maxheight = int(self.trees[row][col])
                    self.visible[row][col] = True
        pass
        for row in range(0,len(self.trees)):
            maxheight = 0
            for col in reversed(range(0,len(self.trees[row]))):
                if int(self.trees[row][col]) > maxheight:
                    maxheight = int(self.trees[row][col])
                    self.visible[row][col] = True
        pass
        for col in range(0,len(self.trees[0])):
            maxheight = 0
            for row in range(0,len(self.trees)):              
                    if int(self.trees[row][col]) > maxheight:
                        maxheight = int(self.trees[row][col])
                        self.visible[row][col] = True
        pass
        for col in range(0,len(self.trees[0])):
            maxheight = 0
            for row in reversed(range(0,len(self.trees))):              
                    if int(self.trees[row][col]) > maxheight:
                        maxheight = int(self.trees[row][col])
                        self.visible[row][col] = True
        pass

    
    def __str__(self) -> str:
        visible=0
        for v in self.visible:
            for x in v:
                visible+=1 if x else 0
        print("visible",visible)
        return "\n".join(self.trees) + "\n\n"+"\n".join((map(lambda s: "".join("T" if a else "F" for a in s), self.visible)))

                


with open('day8.txt', 'r') as file1:
    trees = list(list(map(lambda s: s.strip(),file1.readlines())))
    f = Forerst(trees)
    print(f)
