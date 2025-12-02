# txt = open('2025/02/input_test.txt').read().split()
txt = open('2025/02/input.txt').read().split()

# print(txt)


def part1_repeating_split(num):
    s_num = str(num)
    length = len(s_num)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s_num[:mid]
    second_half = s_num[mid:]
    
    return first_half == second_half

def part1(txt):
    invalid_ids_sum = 0
    id_pair = []
    for line in txt:
        line = line.strip(",").split(",")
        for pair in line:
            pair = pair.split("-")
            id_pair.append((int(pair[0]), int(pair[1])))
    
    for pair in id_pair:
        for num in range(pair[0], pair[1] + 1):
            if part1_repeating_split(num):
                invalid_ids_sum += num

    print(invalid_ids_sum)


def part2_repeating_split(num):
    s_num = str(num)
    length = len(s_num)
    
    for k in range(1, length // 2 + 1):

        if length % k == 0:
            pattern = s_num[:k]
            times_to_repeat = length // k

            if pattern * times_to_repeat == s_num:
                return True

def part2(txt):
    invalid_ids_sum = 0
    id_pair = []
    for line in txt:
        line = line.strip(",").split(",")
        for pair in line:
            pair = pair.split("-")
            id_pair.append((int(pair[0]), int(pair[1])))
    
    for pair in id_pair:
        for num in range(pair[0], pair[1] + 1):
            if part2_repeating_split(num):
                invalid_ids_sum += num

    print(invalid_ids_sum)


part1(txt)
part2(txt)


