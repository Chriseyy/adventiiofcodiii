

# txt = open('2025/inputs/07/input_test.txt').read().split("\n")
txt = open('2025/inputs/07/input.txt').read().split("\n")

def part1(txt):
    grid = [list(line) for line in txt] 
    height = len(grid)
    width = len(grid[0])

    pos_s = None
    splitter = []
    for line_idx, line in enumerate(grid):
        if "S" in line:
            pos_s = [line_idx, line.index("S")]
        for elm_idx, elm in enumerate(line):
            if elm == "^":
                splitter.append([line_idx, elm_idx])
    
    check_stack = [pos_s]
    active_beams = []
    visited_starts = {tuple(pos_s)}

    for pos in check_stack:
        for i in range(height):

            r = pos[0] + i
            c = pos[1]

            if r >= height:
                active_beams.append(((pos[0], pos[1]), (r, c)))
                break

            if [r, c] in splitter:
                active_beams.append(((pos[0], pos[1]), (r, c)))
            
                left = [r, c - 1]
                right = [r, c + 1]
                
                if tuple(left) not in visited_starts and c - 1 >= 0:
                    visited_starts.add(tuple(left))
                    check_stack.append(left) 
                
                if tuple(right) not in visited_starts and c + 1 < width:
                    visited_starts.add(tuple(right))
                    check_stack.append(right) 
                break



    # # andere alternative while loop
    # check_stack = [pos_s]
    # visited_starts = {tuple(pos_s)}
    # active_beams = []
    
    # while len(check_stack) > 0:
    #     pos = check_stack.pop(0) 
        
    #     for i in range(height):
    #         r = pos[0] + i
    #         c = pos[1]
            
    #         if r >= height:
    #             active_beams.append(((pos[0], pos[1]), (r, c)))
    #             break
                
    #         if [r, c] in splitter:
    #             active_beams.append(((pos[0], pos[1]), (r, c)))
                
    #             left = [r, c - 1]
    #             right = [r, c + 1]
                
    #             if tuple(left) not in visited_starts and c - 1 >= 0:
    #                 visited_starts.add(tuple(left))
    #                 check_stack.append(left)
                    
    #             if tuple(right) not in visited_starts and c + 1 < width:
    #                 visited_starts.add(tuple(right))
    #                 check_stack.append(right)
    #             break


    sorted_active_beams = sorted(set(active_beams), key=lambda x: (x[0][1], x[0][0]))

    merged_beams = []
    
    if sorted_active_beams:
        curr_start, curr_end = sorted_active_beams[0]

        curr_col = curr_start[1]
        curr_y_min = curr_start[0]
        curr_y_max = curr_end[0]

        for i in range(1, len(sorted_active_beams)):
            next_start, next_end = sorted_active_beams[i]
            next_col = next_start[1]
            next_y_start = next_start[0]
            next_y_end = next_end[0]

            if next_col == curr_col and next_y_start <= curr_y_max:
                if next_y_end > curr_y_max:
                    curr_y_max = next_y_end
            else:
                merged_beams.append( ((curr_y_min, curr_col), (curr_y_max, curr_col)) )
                curr_col = next_col
                curr_y_min = next_y_start
                curr_y_max = next_y_end

        merged_beams.append( ((curr_y_min, curr_col), (curr_y_max, curr_col)) )

    hit_count = 0
    
    for s_row, s_col in splitter:
        for (start_pos, end_pos) in merged_beams:
            if start_pos[1] == s_col:
                if start_pos[0] <= s_row <= end_pos[0]:
                    hit_count += 1
                    break 

    print("Part 1: ", hit_count)


############################################################

def count_timelines(r, c, memo, height, grid, width):
    if (r, c) in memo:
        return memo[(r, c)]

    curr_r = r
    curr_c = c
    
    while curr_r < height:
        char = grid[curr_r][curr_c]
        
        if char == "^":
            total_paths = 0

            if curr_c - 1 >= 0:
                total_paths += count_timelines(curr_r, curr_c - 1,  memo, height, grid, width)
            
            if curr_c + 1 < width:
                total_paths += count_timelines(curr_r, curr_c + 1,  memo, height, grid, width)
            
            memo[(r, c)] = total_paths
            return total_paths

        curr_r += 1

    return 1

def part2(txt):
    grid = [list(line) for line in txt if line.strip()]
    height = len(grid)
    width = len(grid[0])

    start_pos = None
    for r, line in enumerate(grid):
        if "S" in line:
            start_pos = (r, line.index("S"))
            break

    # Algorithmus: DFS (Depth First Search) mit memoization
    # Algorithmus: DFS (Depth First Search) mit meooization
    result = count_timelines(start_pos[0], start_pos[1], memo = {}, height=height, grid=grid, width=width)
    
    print("Part 2: ", result)





part1(txt)
part2(txt)
