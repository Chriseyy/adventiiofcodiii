
txt = open('2025/inputs/09/input_test.txt').read().split("\n")
# txt = open('2025/inputs/09/input.txt').read().split("\n")


def span_area(p1,p2):
    # count von 0 
    area_x = abs((p1[0]-p2[0]))+1
    area_y = abs((p1[1]-p2[1]))+1
    area = area_x*area_y
    return area

def part1(txt):
    corrds = [pair.split(",") for pair in txt]

    corrds = list(map(lambda x: list(map(int, x)), corrds))
    num_points = len(corrds)

    areas = []
    for i in range(num_points):
        for j in range(i+1, num_points):
            p1 = corrds[i]
            p2 = corrds[j]
            area = span_area(p1,p2)
            areas.append((area, i, j))  

    # for i in areas:
    #     print(i, corrds[i[1]], corrds[i[2]])
    print("Part 1: ", max(areas), corrds[max(areas)[1]], corrds[max(areas)[2]])

############################################

def is_recht_valid(p1, p2, edges):
    # Box von punkten
    px_min = min(p1[0], p2[0])
    px_max = max(p1[0], p2[0])
    py_min = min(p1[1], p2[1])
    py_max = max(p1[1], p2[1])

    # ob wand schneidet senkrecht
    for edge_start, edge_end in edges:
        if edge_start[0] == edge_end[0]: 
            x = edge_start[0]
            y_min_edge = min(edge_start[1], edge_end[1])
            y_max_edge = max(edge_start[1], edge_end[1])
            
            if px_min < x < px_max:
                if max(py_min, y_min_edge) < min(py_max, y_max_edge):
                    return False

        # wand schneidet waagrect
        else: 
            y = edge_start[1]
            x_min_edge = min(edge_start[0], edge_end[0])
            x_max_edge = max(edge_start[0], edge_end[0])
            
            if py_min < y < py_max:
                if max(px_min, x_min_edge) < min(px_max, x_max_edge):
                    return False
                
    # chekcen ob rechteck valid im grünen ist (Ray casting)    
    mid_x = (px_min + px_max) / 2
    mid_y = (py_min + py_max) / 2
    
    schnitt = 0
    for edge_start, edge_end in edges:
        if edge_start[0] == edge_end[0]:
            x = edge_start[0]
            y1 = min(edge_start[1], edge_end[1])
            y2 = max(edge_start[1], edge_end[1])
            
            if y1 < mid_y < y2:
                if x > mid_x:
                    schnitt += 1

    # ungerade anzalhl an wänden ist drinnen 
    return (schnitt % 2) == 1


def span_area(p1,p2):
    area_x = abs((p1[0]-p2[0]))+1
    area_y = abs((p1[1]-p2[1]))+1
    area = area_x*area_y
    return area


def part2(txt):
    corrds = [pair.split(",") for pair in txt]
    corrds = list(map(lambda x: list(map(int, x)), corrds))

    edges = []
    num_points = len(corrds)
    for i in range(num_points):
        p1 = corrds[i]
        p2 = corrds[(i + 1) % num_points]
        edges.append((p1, p2))
    
    print(edges)

    areas = []
    for i in range(num_points):
        for j in range(i+1, num_points):
            p1 = corrds[i]
            p2 = corrds[j]
            
            if is_recht_valid(p1, p2, edges):
                area = span_area(p1, p2)
                areas.append((area, p1, p2)) 

    best = max(areas, key=lambda x: x[0])
    print("Part 2: ", best[0])
    print("corrd:", best[1], best[2])

part1(txt)
print("---------------")
part2(txt)



