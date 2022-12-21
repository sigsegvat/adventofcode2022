class Machine:
    def __init__(self,ops: list[list[str,str]]) -> None:
        self.regXd = 1
        self.regX = 1
        self.ops = ops
        self.cycle=0
        self.current = [next,0]
        self.sum = 0
    
    def tick(self):
        self.cycle+=1
        self.regXd = self.regX
        if self.current[1] == 0 and len(self.ops) >0:
            next = self.ops.pop(0)
            if next[0] == 'noop':
                self.current = [next,0]
            elif next[0] == 'addx':
                self.current = [next,1]
        elif self.current[1] == 1:
            if self.current[0][0] == 'addx':
                self.regX += int(self.current[0][1])
            self.current[1] -= 1
        else:
            self.current[1] -= 1
        if self.cycle in (20,60,100,140,180,220):
            self.sum += self.cycle * self.regXd
    
    def __str__(self) -> str:
        return f"during strenght ({self.cycle}, {self.regXd},{self.cycle * self.regXd}, {self.current}, {self.sum})"

with open('day9.txt', 'r') as file1:
    ops = list(list(map(lambda s: s.strip().split(" "),file1.readlines())))
    m = Machine(ops)
    for i in range(500):
        if i in (20,60,100,140,180,220):
            print(m)
        m.tick()
        #20th, 60th, 100th, 140th, 180th, and 220th cycles
       