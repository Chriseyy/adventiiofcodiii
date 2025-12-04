

# txt = open('2025/inputs/01/input_test.txt').read().split()
txt = open('2025/inputs/01/input.txt').read().split()

# print(txt)

def part1(txt):
    pair_list = []
    for line in txt:
        pair = [line[0], int(line[1:])]
        pair_list.append(pair)

    # print(pair_list)

    # The dial starts by pointing at 50
    start = 50
    zero_count = 0

    for i in pair_list:
        direction = i[0]
        steps = i[1] 
        if direction == 'R':
            start += steps
            if start % 100 == 0:
                zero_count += 1
            if start >= 100:
                start = start % 100

        elif direction == 'L':
            start -= steps
            if start% 100 == 0:
                zero_count += 1
            if start <= 0:
                start = start % 100

    print("---")
    print("Part 1")
    print(start)
    print(zero_count)

def part2(txt):
    pair_list = []
    for line in txt:
        pair = [line[0], int(line[1:])]
        pair_list.append(pair)

    start = 50
    zero_count = 0

    for direction, steps in pair_list:
        for _ in range(steps%100):
            if direction == 'R':
                start += 1
            elif direction == 'L':
                start -= 1
            
            start = start % 100
            if start == 0:
                zero_count += 1
        
        zero_count += steps // 100

    print("---")
    print("Part 2")
    print(start)
    print("Final Zeros:", zero_count)


part1(txt)
part2(txt)

