from random import randint
import turtle

DEAD = ' '
ALIVE = '*'
MAX = 40


def createEmptyGrid():
    g=[]

    for j in range(MAX):
        
        row=[]
        for i in range(MAX):
            row.append(DEAD)
        g.append(row)

    return g

def printGrid(g):
    window=turtle.Screen()
    window.screensize(MAX,MAX)
    turtle.hideturtle()
    turtle.penup()
    
    for i in range(MAX):
       for j in range(MAX):
           if g[i][j]==ALIVE:
                turtle.goto(i,j)
                turtle.dot()


def testTurtle():

    window=turtle.Screen()
    window.screensize(MAX,MAX)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,0)
    turtle.dot()
    turtle.goto(20,20)
    turtle.dot()

    turtle.goto(40,40)
    
    turtle.dot()
    
def createRandomGrid(n):
    g=[]

    for j in range(MAX):
        
        row=[]
        for i in range(MAX):
            x=randint(0,n)
            if x > n/2:
                row.append(ALIVE)
            else:
                row.append(DEAD)
                
        g.append(row)

    return g        

if __name__ == "__main__":   
    grid=createRandomGrid(10)
    
    printGrid(grid)
    #testTurtle()
        
