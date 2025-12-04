use std::{fs};

// &Vec<&str>  oder &[&str]
fn part1(txt: &Vec<&str>) {
    let mut total_joltage: u32 = 0;

    for bank in txt {
        for i in (0..=9).rev() {
            let digit_char = std::char::from_digit(i, 10).unwrap();

            // find index 
            if let Some(number_index) = bank.find(digit_char) {
                // not last digit 
                if number_index < bank.len() - 1 {
                    // rest behind the found digit
                    let string_behind = &bank[number_index + 1..];
                    
                    // find max remaining string
                    if let Some(next_biggest) = string_behind.chars().max() {
                        let num_str = format!("{}{}", digit_char, next_biggest);
                        total_joltage += num_str.parse::<u32>().unwrap();
                        
                        break;
                    }
                }
            }
        }
    }

    println!("Part 1 Total: {}", total_joltage);
}



fn part2(txt: &Vec<&str>) {
    let mut total_joltage: u64 = 0;
    let target_length= 12;

    for bank in txt {

        if bank.len() < target_length {
            continue; 
        }

        let mut move_right_possible = bank.len() - target_length;

        // let mut stack = vec![]; selbe fast
        let mut stack: Vec<char> = Vec::new();
    
        for number in bank.chars() {
            while !stack.is_empty() && *stack.last().unwrap() < number && move_right_possible > 0 {
                stack.pop();
                move_right_possible -= 1;
            }
            stack.push(number);
        }

        // truncate target length
        if stack.len() > target_length {
            stack.truncate(target_length);
        }

        let result_string: String = stack.iter().collect();
        if let Ok(val) = result_string.parse::<u64>() {
            total_joltage += val;
        }
    }

    println!("Part 2 Total: {}", total_joltage);
}


fn main() {
    let content = fs::read_to_string("inputs/03/input.txt").expect("file?");
    let txt: Vec<&str> = content.split_whitespace().collect();

    part1(&txt);
    part2(&txt);
}