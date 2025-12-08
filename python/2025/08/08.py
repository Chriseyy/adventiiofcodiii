
# txt = open('2025/inputs/08/input_test.txt').read().split("\n")
txt = open('2025/inputs/08/input.txt').read().split("\n")


def distance(p1,p2):
    dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
    dist = dist_sq ** 0.5
    return dist


def part1(txt, target_connections=10):
    points = []
    for line in txt:
        coords = list(map(int, line.split(',')))
        points.append(tuple(coords))

    distances_edges = []
    num_points = len(points)

    for i in range(num_points):
        for j in range(i+1, num_points):
            p1 = points[i]
            p2 = points[j]
            dist = distance(p1,p2)
            distances_edges.append((dist, i, j))      

    distances_edges.sort()

    circuit_id = list(range(num_points))

    edges = distances_edges[:target_connections]

    for dist, i, j in edges:
        circuit_i = circuit_id[i]
        circuit_j = circuit_id[j]
        
        if circuit_i != circuit_j:
            for k in range(num_points):
                if circuit_id[k] == circuit_j:
                    circuit_id[k] = circuit_i

    circuit_count = {}
    for circ_id in circuit_id:
        if circ_id not in circuit_count:
            circuit_count[circ_id] = 0
        circuit_count[circ_id] += 1

    all_sizes = list(circuit_count.values())
    all_sizes.sort(reverse=True)

    print("\nErgebnis:")
    print(f"circuit size: {all_sizes}")

    product = all_sizes[0] * all_sizes[1] * all_sizes[2]
    print(f"part 1: three largest circuits top3: {product}")




def part2(txt, target_connections=10):
    points = []
    for line in txt:
        coords = list(map(int, line.split(',')))
        points.append(tuple(coords))

    distances_edges = []
    num_points = len(points)

    for i in range(num_points):
        for j in range(i+1, num_points):
            p1 = points[i]
            p2 = points[j]
            dist = distance(p1,p2)
            distances_edges.append((dist, i, j))      

    distances_edges.sort()

    circuit_id = list(range(num_points))
    num_clusters = num_points

    for dist, i, j in distances_edges:
        circuit_i = circuit_id[i]
        circuit_j = circuit_id[j]
        
        if circuit_i != circuit_j:
            for k in range(num_points):
                if circuit_id[k] == circuit_j:
                    circuit_id[k] = circuit_i
            
            num_clusters -= 1

        if num_clusters == 1:
            x1 = points[i][0]
            x2 = points[j][0]
            result = x1 * x2
            
            print(f"p1_X: {x1}")
            print(f"p2_X: {x2}")
            print(f"Part 2: {result}")
            break


# part1(txt,target_connections=10)
part1(txt,target_connections=1000)
print("----")
part2(txt)



