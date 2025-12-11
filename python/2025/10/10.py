
# txt = open('2025/inputs/10/input_test.txt').read().split("\n")
txt = open('2025/inputs/10/input.txt').read().split("\n")

def part1(txt):
    total_presses = 0

    for line in txt:
        parts = line.split()
        target_str = parts[0].replace('[', '').replace(']', '')

        target_bit_number = 0
        for i in range(len(target_str)):
            if target_str[i] == '#':
                # wandeln input in bit um alos .##. in 6 
                # << bedeutet nimm die 1 und schibe nach links also: i = 0: 0001 (Zahl 1) oder i = 2: 0100 (Zahl 4)
                # | ist bitwise OR oder vergliecht zalen auf bit ebene und irgendwo eine 1 ist das Ergebnis dort auch 1 bsp. 0010 | 0100 -> 0110
                target_bit_number = target_bit_number | (1 << i)

        buttons = []
        for buttons_str in parts[1:-1]:
            clean = buttons_str.replace('(', '').replace(')', '')
            indices = clean.split(',')
            
            buttons_mask = 0
            for idx in indices:
                # bit an der der den stellen asnacheln also 1,3 and stelle .#.# also also 10
                # << bedeutet nimm die 1 und schibe nach links also: i = 0: 0001 (Zahl 1) oder i = 2: 0100 (Zahl 4)
                buttons_mask = buttons_mask | (1 << int(idx))
            buttons.append(buttons_mask)
            
        # BFS Breadth-First Search (BFS). für küzestes weg
        current_layer = [0]
        visited = {0}
        steps = 0
        found = False
        
        while not found and len(current_layer) > 0:
            next_layer = []
            
            for state in current_layer:
                # akutelle nummer gleich target number 
                if state == target_bit_number:
                    total_presses += steps
                    found = True
                    break
                
                for btn in buttons:
                    # ^ ist XOR (Exlusives Oder) passt logik an bsp. 0^1 = 1 licht off, Knopf press -> on)
                    new_state = state ^ btn
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        next_layer.append(new_state)
            
            # wichtig um an wengists knopf drücke zu fidnen 
            # also nehmen die ergebnisse und drücken nochmal jeden knopf
            # so lange bis found = True in if state == target_bit_number:
            current_layer = next_layer  
            if not found:
                steps += 1

    print("part1: ", total_presses)


def part2(txt):
    total_presses = 0

    for line in txt:
        if not line.strip():
            continue

        parts = line.split()
        
        # {3,5,4,7} 
        joltage_str = parts[-1].replace('{', '').replace('}', '')
        
        # (3, 5, 4, 7)
        target_tuple = tuple(int(x) for x in joltage_str.split(','))
        num_counters = len(target_tuple)

        # Knopf aufaddiert
        # knopf (1,3) - 4 Countern [0, 1, 0, 1]
        buttons = []
        for btn_str in parts[1:-1]:
            clean = btn_str.replace('(', '').replace(')', '')
            indices = clean.split(',')
            
            btn_effect = [0] * num_counters  # [0, 0, 0, 0]
            for idx in indices:
                btn_effect[int(idx)] = 1
            
            buttons.append(tuple(btn_effect))  # [0, 1, 0, 1]

        # BFS ruckwärts (subtraktion
        current_layer = [target_tuple]  # [(3, 5, 4, 7)]
        visited = {target_tuple}
        steps = 0
        found = False
        
        while not found and len(current_layer) > 0:
            next_layer = []
            
            for current_state in current_layer:
                # wir [0, 0, 0...] erreicht
                # sum(current_state) == 0 prüft alle Einträge 0 sind (da keine negativen)
                if sum(current_state) == 0:   # 0+0+0+0 ist 0
                    total_presses += steps
                    found = True
                    break
                
                # Knopf rückwärts drücken (abziehen)
                for btn in buttons:
                    # current - button
                    new_state_list = []
                    valid_move = True
                    
                    for i in range(num_counters):
                        val = current_state[i] - btn[i]   #  (3, 5, 4, 7) -[0, 1, 0, 1] =  (3, 4, 4, 6)
                        if val < 0:
                            # unter 0 -> dieser Weg Sackgasse
                            valid_move = False
                            break
                        new_state_list.append(val)
                    
                    if valid_move:
                        new_state_tuple = tuple(new_state_list)
                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)    # spriehcen (3, 4, 4, 6)
                            next_layer.append(new_state_tuple)
            
            current_layer = next_layer
            if not found:
                steps += 1
                
        if not found:
            print(f"Warnung: Keine Lösung für {target_tuple} gefunden!")

    print("Part 2: ", total_presses)


part1(txt)
part2(txt)



