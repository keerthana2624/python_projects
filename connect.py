def initialize_grid(n, m):
    grid = []
    for i in range(n):
        r = []
        for j in range(m):
            r.append(0)
        grid.append(r)
    return grid

def display_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
    print()  
def handle_user_input(grid):
    while True:
        try:
            c = int(input("Enter the column you want to place the disc (0-6): "))
            if 0 <= c < len(grid[0]):
                if grid[0][c] == 0:
                    return c
                else:
                    print("Column is full. Try another column.")
            else:
                print("Column is out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def drop_disc(grid, player, c):
    for i in range(len(grid)-1, -1, -1):
        if grid[i][c] == 0:
            grid[i][c] = player
            break
    return grid

def check_win(grid, player):
    r = len(grid)
    c = len(grid[0])
    
    for i in range(r):
        for j in range(c-3):
            if grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == player:
                return True
    
    for i in range(c):
        for j in range(r-3):
            if grid[j][i] == grid[j+1][i] == grid[j+2][i] == grid[j+3][i] == player:
                return True
            
    for i in range(r-3):
        for j in range(c-3):
            if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == player:
                return True
    for i in range(3, r):
        for j in range(c-3):
            if grid[i][j] == grid[i-1][j+1] == grid[i-2][j+2] == grid[i-3][j+3] == player:
                return True
                
    return False

def check_draw(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

def switch_player(player):
    return 2 if player == 1 else 1

def main():
    print("Welcome to the Connect Four game")
    grid = initialize_grid(6, 7)
    display_grid(grid)
    player = 1
    
    while True:
        print(f"It is player {player}'s turn.")
        c = handle_user_input(grid)
        grid = drop_disc(grid, player, c)
        display_grid(grid)
        
        if check_win(grid, player):
            print(f"Congratulations! Player {player} wins!")
            break
        elif check_draw(grid):
            print("It's a tie!")
            break
        
        player = switch_player(player)

main()