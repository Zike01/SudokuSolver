import pyautogui as pg
import time

def possible(x,y,n):
    # check row
    for i in range(9):
        if grid[x][i] == n:
            return False
        
    # check column
    for i in range(9):
        if grid[i][y] == n:
            return False
        
    # check square
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == n:
                return False      
    return True


def fill_grid(matrix):
    print("click the top left tile of the sudoku puzzle")
    time.sleep(1)
    
    for i in range(3,0,-1):
        print(f"{i}")
        time.sleep(1)
        
    final_inputs = []
    for row in matrix:
        for elt in row:
            final_inputs.append(str(elt))

    counter = 0
    for num in final_inputs:
        pg.press(num)
        pg.press("right")
        counter += 1

        if counter % 9 == 0:
            pg.press("down")
            for _ in range(8):
                pg.press("left")


def solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    fill_grid(grid)


if __name__ == "__main__":
    grid = []
    for i in range(9):
        row = []

        while len(row) != 9:
            row = [int(n) for n in list(input(f"Row {i+1}: "))]
        grid.append(row)
        print(f"row {i+1} complete")
    solve()
