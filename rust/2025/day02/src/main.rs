use std::{fs};


fn part1_repeating_split(num: u64) -> bool {
    let s_num = num.to_string();
    let length = s_num.len();

    if length % 2 != 0 {
        return false;
    }

    let mid = length / 2;
    let first_half = &s_num[..mid];
    let second_half = &s_num[mid..];

    first_half == second_half
}

fn part1(ranges: &Vec<(u64, u64)>) {
    let mut invalid_ids_sum: u64 = 0;
    for &(start, end) in ranges {
        for num in start..=end {
            if part1_repeating_split(num) {
                invalid_ids_sum += num;
            }
        }
    }

    println!("Part 1 sum: {}", invalid_ids_sum);
}


//-----------------------------

fn part2_repeating_split(num: u64) -> bool {
    let s_num = num.to_string();
    let length = s_num.len();

    for k in 1..=(length / 2) {
        if length % k == 0 {
            let pattern = &s_num[..k];
            let times_to_repeat = length / k;

            if pattern.repeat(times_to_repeat) == s_num {
                return true;
            }
        }
    }
    false
}

fn part2(ranges: &Vec<(u64, u64)>) {
    let mut invalid_ids_sum: u64 = 0;

    for &(start, end) in ranges {
        for num in start..=end {
            if part2_repeating_split(num) {
                invalid_ids_sum += num;
            }
        }
    }

    println!("Part 2 sum: {}", invalid_ids_sum);
}


//-----------------------------



fn main() {
    let content = fs::read_to_string("inputs/02/input.txt").expect("file?");

    let mut ranges: Vec<(u64, u64)> = Vec::new();

    for line in content.split_whitespace() {
        let parts = line.trim_matches(',').split(',');
        
        for part in parts {
            if part.is_empty() { continue; }
            
            // .collect() creates a vector from the iterator wichtiggggg
            // Referneze
            let pair: Vec<&str> = part.split('-').collect();
            //oder kopieren
            // let pair: Vec<String> = part.split('-').map(|s| s.to_string()).collect();
            
            if pair.len() == 2 {
                let start: u64 = pair[0].parse().unwrap();
                let end: u64 = pair[1].parse().unwrap();
                ranges.push((start, end));
            }
        }
    }
    part1(&ranges);
    part2(&ranges);
}