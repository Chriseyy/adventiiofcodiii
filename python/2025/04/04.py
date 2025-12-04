txt = open('2025/inputs/04/input_test.txt').read().split()
# txt = open('2025/inputs/04/input.txt').read().split()


def check_field(grid, row, col):
    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    
    if grid[row][col] == '@':
        neighbors = 0
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == '@':
                    neighbors += 1

        if neighbors < 4:
            return True

def part1(txt):
    grid = []
    row = []
    for line in txt:
        for x in line:
            row.append(x)
        grid.append(row)
        row = []    

    # grid = [list(line) for line in txt] kompakter

    forklift_accesable = 0
    for idx_row, row in enumerate(grid):
        for idx_col, col in enumerate(row):
            if check_field(grid, idx_row, idx_col):
                forklift_accesable += 1

    print(forklift_accesable)


##############################################


def part2(txt):
    grid = []
    row = []
    for line in txt:
        for x in line:
            row.append(x)
        grid.append(row)
        row = []    
        
    
    forklift_accesable = 0
    update_possible = True
    while update_possible:
        update_list = []
        grid = [r.copy() for r in grid]
        for idx_row, row in enumerate(grid):
            for idx_col, col in enumerate(row):
                if check_field(grid, idx_row, idx_col):
                    forklift_accesable += 1
                    update_list.append((idx_row, idx_col))

        if update_list == []:
            update_possible = False
        for update in update_list:
            grid[update[0]][update[1]] = '.'


    print(forklift_accesable)



part1(txt)
part2(txt)




