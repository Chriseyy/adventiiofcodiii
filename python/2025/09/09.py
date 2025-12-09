
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

def span_area(p1,p2):
    # count von 0 
    area_x = abs((p1[0]-p2[0]))+1
    area_y = abs((p1[1]-p2[1]))+1
    area = area_x*area_y
    return area

def part2(txt):
    corrds = [pair.split(",") for pair in txt]

    corrds = list(map(lambda x: list(map(int, x)), corrds))

    num_points = len(corrds)

    allowed_area = [corrds]

    green_tils = []

    for i in corrds:
        print(i)


    # areas = []
    # for i in range(num_points):
    #     for j in range(i+1, num_points):
    #         p1 = corrds[i]
    #         p2 = corrds[j]
    #         area = span_area(p1,p2)
    #         areas.append((area, i, j))  

    # # for i in areas:
    # #     print(i, corrds[i[1]], corrds[i[2]])
    # print(max(areas), corrds[max(areas)[1]], corrds[max(areas)[2]])


part1(txt)
part2(txt)



