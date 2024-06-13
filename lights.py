import random
def initialize_grid():
    grid=[]
    for i in range(5):
        row=[]
        for j in range(5):
            x=random.choice([1,0])
            row.append(x) 
        grid.append(row)   
    return grid

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j,end="  ")
        print()
# print_grid(initialize_grid())

def get_user():
    while True:
        try:
            row=int(input("please enter your row: "))
            if 0<=row<=4:
                while True:
                    try:
                        col=int(input("please enter your col position: "))
                        if 0<=col<=4:
                            return row,col
                        else:
                            print("Invalid col position")
                    except:
                        print("enter valid light positions")
                
            else:
                print("Invalid row position")
        except ValueError:
            print("enter valid light positions")

def toggle_light(grid,row,col):
    # Top light
    if row>0: 
        if grid[row-1][col]==0:
            grid[row-1][col]=1
        else:
            grid[row-1][col]=0
    # Bottom light
    if row<4:
        if grid[row+1][col]==0:
            grid[row+1][col]=1
        else:
            grid[row+1][col]=0
    # left light
    if col>0:
        if grid[row][col-1]==0:
            grid[row][col-1]=1
        else:
            grid[row][col-1]=0

    # right light
    if col<4:
        if grid[row][col+1]==0:
            grid[row][col+1]=1
        else:
            grid[row][col+1]=0

    if grid[row][col]==0:
            grid[row][col]=1
    else:
        grid[row][col]=0
    return grid
        