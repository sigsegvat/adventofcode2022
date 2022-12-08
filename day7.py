

class Dir:
    def __init__(self, name, parent) -> None:
        self.name=name
        self.size=0
        self.subdirs=[]
        self.parent=parent
        pass

    def file(self,filename,size):
        self.size+=size
    
    def adddir(self,name):
        a = Dir(name,self)
        self.subdirs.append(a)
        return a
    
    def path(self):
        if(self.parent == None):
            return self.name
        else:
            return self.parent.path() + "/" + self.name

    def calc_size(self):
        return self.size + sum(d.calc_size() for d in self.subdirs)
    
    def traverse(self):
        csize= self.calc_size()
        if csize > 3598596:
            print(self.calc_size(),self.path())
        for s in self.subdirs:
            s.traverse()
    




with open('day7.txt', 'r') as file1:
    lines = list(map(str.strip,file1.readlines()))
    root = Dir("/", None)
    e = root
    for line in lines:
        if line.startswith("$ cd"):
            dirname = line[5:]
            if dirname == "/":
                e = root
            elif dirname == "..":
                e = e.parent
            else:
                e = e.adddir(dirname)
        elif line.startswith("$ ls"):
            pass
        else:
            (a,name) = line.split(" ")
            if(a != "dir"):
                e.file(name,int(a))
        

print(30000000-(70000000-root.calc_size()))
root.traverse()