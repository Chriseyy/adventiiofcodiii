

# txt = open('2025/inputs/06/input_test.txt').read().split("\n")
txt = open('2025/inputs/06/input.txt').read().split("\n")




def part1(txt):
    plus_or_muls = [i for i in txt[-1] if i != " "]
    problems_list = []

    for row in txt[0:len(txt)-1]:
        row = row.split(" ")
        clean_row = [i for i in row if i != ""] 
        problems_list.append(clean_row)

    end_sum = 0
    for idx, elm in enumerate(plus_or_muls):
        if elm == "+":
            end_sum += sum(int(i[idx]) for i in problems_list)

        if elm == "*":
            multi_sum = 1
            multi = [int(i[idx]) for i in problems_list]
            for i in multi:
                multi_sum *= i
            end_sum += multi_sum


    print("Part 1: ",end_sum)


def part2(txt):
    max_len = max(len(line) for line in txt)
    grid = [line for line in txt] 

    # print(max_len)

    end_sum = 0
    temp_problem_numbers = []
    plus_mul_operator = None

    for x in range(max_len-1, -1, -1):
        # zahl von recht nach links
        col_str = ""
        for i in grid[0:(len(grid)-1)]:
            col_str += i[x]

        if col_str.strip() == "":
            if temp_problem_numbers:
                if plus_mul_operator == '+':
                    result = sum(temp_problem_numbers)

                elif plus_mul_operator == '*':
                    mul_num = 1
                    for i in temp_problem_numbers:
                        mul_num *= i
                    

                    result = mul_num 
                
                else:
                    result = 0

                end_sum += result
                temp_problem_numbers = []
                plus_mul_operator = None
                
            continue

        number = int(col_str)
        temp_problem_numbers.append(number)

        op_char = grid[-1][x]
        if op_char in ('+', '*'):
            plus_mul_operator = op_char

    if temp_problem_numbers:
        if plus_mul_operator == '+':
            end_sum += sum(temp_problem_numbers)
        elif plus_mul_operator == '*':
            mul_num = 1
            for i in temp_problem_numbers:
                mul_num *= i
            end_sum += mul_num

    print(f"Part 2: {end_sum}")


part1(txt)
part2(txt)
