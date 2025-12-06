use std::{fs};

fn part1(content: &str) {

    let lines: Vec<&str> = content.lines().filter(|l| !l.trim().is_empty()).collect();
    // Vec nur printbar mit {:?}  
    // println!("{:?}", lines);

    // if lines.is_empty() { return 0; }    best pratice 

    // operatoren , zahlen davor 
    let (op_line, number_lines) = lines.split_last().unwrap();
    // println!("{}",op_line);
    // println!("{:?}",number_lines);

    let grid: Vec<Vec<u64>> = number_lines.iter()
        .map(|line| {
            line.split_whitespace()
                .filter_map(|n| n.parse::<u64>().ok())
                .collect()
        })
        .collect();

    let operators: Vec<&str> = op_line.split_whitespace().collect();

    let mut end_sum: u64 = 0;

    for (col_idx, operator) in operators.iter().enumerate() {
        let col_vlaues = grid.iter().map(|row| row[col_idx]);


        // If alternaitve funnnny
        match *operator {
            "+" => {
                end_sum += col_vlaues.sum::<u64>();
            },
            "*" => {
                end_sum += col_vlaues.product::<u64>();
            },
            _ => panic!("Unbekannter Operator: {}", operator),
        }
    }

    println!("Part 1: {}", end_sum);
        
}



fn main() {
    let content = fs::read_to_string("inputs/06/input.txt").expect("file?");

    part1(&content);
}