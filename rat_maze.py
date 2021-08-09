class Maze:
    def __init__(self,m,n):
        self.m=m
        self.n=n
        self.m1=[[False for i in range(self.n)]for j in range(self.n)]
        self.x=0
        self.y=0
        self.solution=[]
        self.m1[0][0]=True
        #print(self.m1)
        self.solve(0,0)
    def solve(self,x,y):
        if x==self.n-1 and y == self.n-1:
            self.display()
            self.reverse(x,y)
        elif ( x < self.n and y < self.n):
            if self.safe(x+1,y):
                self.solution.append("D")
                #print(self.solution)
                self.move(x+1,y)
                self.solve(x+1,y)
            if self.safe(x,y+1):
                self.solution.append("R")
                #print(self.solution)
                self.move(x,y+1)
                self.solve(x,y+1)
            if self.safe(x-1,y):
                self.solution.append("U")
                #print(self.solution)
                self.move(x-1,y)
                self.solve(x-1,y)
            if self.safe(x,y-1):
                self.solution.append("L")
                #print(self.solution)
                self.move(x,y-1)
                self.solve(x,y-1)
            
            self.reverse(x,y)

    def display(self):
            print("".join(self.solution))
    def safe(self,x,y):
        if (x<self.n and x>=0) and (y<self.n and y >=0):
            return not self.m1[x][y] and self.m[x][y]
        else:
            return 0
            
    def move(self,x,y):
        self.x=x
        self.y=y
        self.m1[x][y]=True

    def reverse(self,x,y):
        if x==0 and y ==0:
            return
        self.solution.pop()
        self.m1[x][y]=False
        #print(self.solution)
                
maze=[ [ 1, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1 ],
          [ 1, 1, 1, 0, 1 ],
          [ 0, 0, 0, 0, 1 ],
          [ 0, 0, 0, 0, 1 ] ]          
m=Maze(maze,len(maze))



