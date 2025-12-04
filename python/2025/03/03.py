# txt = open('2025/inputs/03/input_test.txt').read().split()
txt = open('2025/inputs/03/input.txt').read().split()


def part1(txt):
    total_joltage = 0
    for bank in txt:
        for i in range(9, -1, -1):
            number_index = bank.find(str(i))
            if number_index != -1 and number_index < len(bank) - 1:
                string_behind_number = bank[number_index+1:]
                next_biggest_number = max(string_behind_number)

                total_joltage += int(str(i) + next_biggest_number)
                break
                # return int(str(i) + next_biggest_number)

    print(total_joltage)
    # return 0


def part2(txt):
    total_joltage = 0
    for bank in txt:
        target_length = 12
        move_right_possible = len(bank) - target_length
        stack = []
        for number in bank:
            while stack and stack[-1] < number and move_right_possible > 0:
                stack.pop()
                move_right_possible -= 1

            stack.append(number)
        
    
        result_string = "".join(stack[:target_length])
        total_joltage += int(result_string)
        
    print(total_joltage)

part1(txt)
part2(txt)


# total_joltage = 0
# for bank in txt:
#     total_joltage += part1(bank)

# print(total_joltage)




