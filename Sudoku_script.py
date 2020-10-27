import numpy as np
import pandas as pd
import sys

#importing matrix
grid = pd.read_excel(r"C:\Users\Shivam\Desktop\puzzle.xlsx",header=None,index_col=False)
grid.fillna(0,inplace=True)
grid=np.matrix(grid.to_numpy(dtype='int'))


#function to check possiblity of inserstion based on rules of the game. Checks only one digit n at (x,y)

def possible(y,x,n):
    global grid
    if (grid[y:y+1,:]==n).any():
        return False
    if (grid[:,x:x+1]==n).any():
        return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    if (grid[y0:y0+3,x0:x0+3]==n).any():
        return False
    return True

#Function to solve the puzzle in the global variable grid
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y,x]==0:
                for n in range(10):
                    if possible(y,x,n):
                        grid[y,x]=n
                        solve()
                        grid[y,x]=0
                return
    print(grid)
    sys.exit()


solve()