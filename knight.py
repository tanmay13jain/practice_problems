class Knight:
    def __init__(self,n):
        self.n=n
        self.count=0
        self.grid=[[False for i in range(self.n)]for j in range(self.n)]
        self.matrix=[[False for i in range(self.n)]for j in range(self.n)]
        self.grid[0][0] = True
        self.matrix[0][0] = True
        self.solve(0,0)
    def solve(self,x,y):
        
        if ( x>=0 and x < self.n) and (y>=0 and y < self.n):
            if self.safe(x+1,y+2):
                self.insert(x+1,y+2)
                self.solve(x+1,y+2)
            if self.safe(x+1,y-2):
                self.insert(x+1,y-2)
                self.solve(x+1,y-2)
            if self.safe(x-1,y+2):
                self.insert(x-1,y+2)
                self.solve(x-1,y+2)
            if self.safe(x-1,y-2):
                self.insert(x-1,y-2)
                self.solve(x-1,y-2)
            if self.safe(x+2,y+1):
                self.insert(x+2,y+1)
                self.solve(x+2,y+1)
            if self.safe(x+2,y-1):
                self.insert(x+2,y-1)
                self.solve(x+2,y-1)
            if self.safe(x-2,y+1):
                self.insert(x-2,y+1)
                self.solve(x-2,y+1)
            if self.safe(x-2,y-1):
                self.insert(x-2,y-1)
                self.solve(x-2,y-1)
            self.remove(x,y)
    def safe(self,x,y):
        if ( x>=0 and x<self.n) and (y>=0 and y<self.n):
            return not self.grid[x][y] and not self.matrix[x][y]
    def display(self,m):
        for i in range(self.n):
            for j in range(self.n):
                if i == 0 and j == 0:
                    print (0,end ="  ")
                else:
                    if m[i][j]<10:      #for perfect printing indentation
                        print(m[i][j],end="  ")
                    else:
                        print (m[i][j],end=" ")
            print()
        
            
    def remove(self,x,y):
        if self.count == (self.n**2)-1:
            return
            
        if x == 0 and y == 0:
            return
        self.grid[x][y]=False
        self.matrix[x][y]=False
        self.count-=1 
    
    def insert(self,x,y):
        
        self.grid[x][y]=True
        self.count+=1
        self.matrix[x][y]=self.count
        
N=6
k=Knight(N)
k.display((k.matrix))
