
use std::{fs};

fn part1() {
    let input = fs::read_to_string("day01/src/input.txt").expect("Not found");

    let mut position: i32 = 50; 
    let mut zero_hits = 0;

    for line in input.lines() {
        if line.is_empty() { continue; }
        // + oder - L oder R
        let direction = line.chars().next().unwrap();

        // zahl danach i32 geht in plus und minus   gibt auch u32 aber mach kein minus breich
        let amount: i32 = line[1..].parse().expect("Keine Zahl gefunden");

        if direction == 'R' {
            position += amount;
        } else {
            position -= amount;
        }

        position = position.rem_euclid(100);


        // println!("Bewege {} um {} - Lande {}", direction, amount, position);

        if position == 0 {
            zero_hits += 1;
        }
}

    println!("Part 1 - Zeros: {}", zero_hits);
}


fn part2() {
    let input = fs::read_to_string("day01/src/input.txt").expect("Not found");

    let mut position: i32 = 50; 
    let mut zero_hits = 0;

    for line in input.lines() {
        if line.is_empty() { continue; }
        // + oder - L oder R
        let direction = line.chars().next().unwrap();

        // zahl danach i32 geht in plus und minus   gibt auch u32 aber mach kein minus breich
        let amount: i32 = line[1..].parse().expect("Keine Zahl gefunden");

        zero_hits += amount / 100; 

        for _ in 0..amount.rem_euclid(100) {
            if direction == 'R' {
                position += 1;
            } else {
                position -= 1;
            }

            position = position.rem_euclid(100);

            if position == 0 {
                zero_hits += 1;
            }

        }
    }
    println!("Part 2 - Zeros: {}", zero_hits);
}


fn main() {
    part1();
    part2();
}