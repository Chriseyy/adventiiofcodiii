

# txt = open('2025/inputs/05/input_test.txt').read().split("\n")
txt = open('2025/inputs/05/input.txt').read().split("\n")

def check_range(ranges, ingredient_id):
    for r in ranges:
        low = int(r[0])
        high = int(r[1])
        if low <= ingredient_id <= high:
            return True
    return False

def part1(txt):
    fresh_ingredients = 0
    fresh_range = []
    ingredient_ids = []
    space_idx = txt.index('')
    
    for ranges_pair in txt[0:space_idx]:
        pair = ranges_pair.split('-')
        fresh_range.append(pair)

    for ingredient in txt[space_idx+1:]:
        ingredient_ids.append(int(ingredient))
    

    for ingredient_id in ingredient_ids:
        if check_range(fresh_range, ingredient_id):
            fresh_ingredients += 1

    print("Part 1: ", fresh_ingredients)


##########################################



def part2(txt):
    fresh_ranges = []
    space_idx = txt.index('')
    
    for ranges_pair in txt[0:space_idx]:
        pair = ranges_pair.split('-')
        start = int(pair[0])
        end = int(pair[1])
        fresh_ranges.append([start, end])

    fresh_ranges.sort(key=lambda x: x[0])

    merged_ranges = []

    if fresh_ranges:
        cur_start, cur_end = fresh_ranges[0]
    
        for i in range(1, len(fresh_ranges)):
            next_start, next_end = fresh_ranges[i]
            
            if next_start <= cur_end + 1: # 3-5+1 und 6-8 wegen +1 overlap -> mergen
                cur_end = max(cur_end, next_end)
            else:
                merged_ranges.append((cur_start, cur_end))
                cur_start, cur_end = next_start, next_end
        
        merged_ranges.append((cur_start, cur_end))

    all_ranges_count = 0
    for start, end in merged_ranges:
        all_ranges_count += (end-start+1)

    print("Part 2: ", all_ranges_count)

part1(txt)
part2(txt)
