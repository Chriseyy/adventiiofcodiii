
# txt = open('2025/inputs/11/input_test.txt').read().split("\n")
txt = open('2025/inputs/11/input.txt').read().split("\n")


def count_paths(current_node, graph, memo):
    if current_node == 'out':
        return 1
    
    if current_node in memo:
        return memo[current_node]
    
    if current_node not in graph:
        return 0

    total_paths = 0
    for neighbor in graph[current_node]:
        total_paths += count_paths(neighbor, graph, memo)
    
    memo[current_node] = total_paths
    return total_paths


def part1(txt):
    graph = {}

    for line in txt:
        parts = line.split(":")
        node = parts[0].strip()
        neighbors = parts[1].strip().split()
        graph[node] = neighbors

    # print(graph)

    memo = {}
    #DFS mit Memoization
    anzahl_wege = count_paths('you', graph, memo)

    print("part1: ", anzahl_wege)


#################################################################

def get_permutations(elements):
    if len(elements) <= 1:
        return [elements]
    
    perms = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        
        for p in get_permutations(remaining):
            perms.append([current] + p)
    return perms


def count_paths_2(current, target, graph, memo):
    if current == target:
        return 1
    if current in memo:
        return memo[current]
    if current not in graph:
        return 0
    total = 0
    for neighbor in graph[current]:
        total += count_paths_2(neighbor, target, graph, memo)
    memo[current] = total
    return total

def part2(txt):
    graph = {}

    for line in txt:
        parts = line.split(":")
        node = parts[0].strip()
        neighbors = parts[1].strip().split()
        if len(parts) > 1:
            neighbors = parts[1].strip().split()
            graph[node] = neighbors
        else:
            graph[node] = []


    start_node = 'svr'
    end_node = 'out'
    must_visit = ['dac', 'fft']

    visit_orders = get_permutations(must_visit)

    grand_total = 0

    for order in visit_orders:
        full_route = [start_node] + order + [end_node]
        
        paths_for_this_route = 1
        valid_route = True
        
        for i in range(len(full_route) - 1):
            segment_start = full_route[i]
            segment_end = full_route[i+1]
            
            memo = {}
            count = count_paths_2(segment_start, segment_end, graph, memo)
            
            if count == 0:
                valid_route = False
                paths_for_this_route = 0
                break
                
            paths_for_this_route *= count
        
        if valid_route:
            route_str = " -> ".join(full_route)
            print(f"Route: {route_str} | wege: {paths_for_this_route}")
            grand_total += paths_for_this_route

    print("Part2: ",grand_total)

part1(txt)

part2(txt)
