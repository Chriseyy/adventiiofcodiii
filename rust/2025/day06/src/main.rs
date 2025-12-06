use std::{fs};

fn part1(content: &str) {

    let lines: Vec<&str> = content.lines().filter(|l| !l.trim().is_empty()).collect();
    // Vec nur printbar mit {:?}  
    // println!("{:?}", lines);


    // ohne .iter geht der print dananch nicht mehr :D
    // der print println!("{:?}", lines); geht mit lines.iter() oder &lines
    // iter_mnut wenn ihcdas im vektor ändern will elemnte 
    // for line in lines.iter(){
    //     println!("{}", line);
    // }

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


//---------------------------

fn process_group(numbers: &mut Vec<u64>, op: Option<char>) -> u64 {
    if numbers.is_empty() { return 0; }
    
    let result = match op {
        Some('+') => numbers.iter().sum::<u64>(),
        Some('*') => numbers.iter().product::<u64>(),
        _ => 0, 
    };
    
    numbers.clear(); // Wichtig: Der Vektor wird geleert!
    result
}

fn part2(content: &str) {

    let grid: Vec<Vec<char>> = content.lines()
            .filter(|l| !l.is_empty()) 
            .map(|l| l.chars().collect())
            .collect();
    
    // println!("{:?}", grid);

    let max_len = grid.iter().map(|row| row.len()).max().unwrap_or(0);
    
    let height = grid.len();

    let mut end_sum: u64 = 0;
    let mut temp_promblem_numbers: Vec<u64> = Vec::new();
    let mut current_operator = None;    // Option<char>

    // // Closures oder mache das außerhalb als fn funktion nicht drinnen find es komsich hat ki als optimierung Closures das darunter vorgeschlagen 
    // let process_group = |numbers: &mut Vec<u64>, op: Option<char>| -> u64 {
    //     if numbers.is_empty() { return 0; }
        
    //     let result = match op {
    //         Some('+') => numbers.iter().sum::<u64>(),
    //         Some('*') => numbers.iter().product::<u64>(),
    //         _ => 0, 
    //     };
        
    //     numbers.clear(); 
    //     result
    // };


    for x in (0..max_len).rev() {
        let mut col_str = String::new();
        for y in 0..height-1 {
            let char_pos = grid[y].get(x).unwrap_or(&' ');
            col_str.push(*char_pos);
        }

        if col_str.trim().is_empty() {
            if !temp_promblem_numbers.is_empty() {
                end_sum += process_group(&mut temp_promblem_numbers, current_operator);
                current_operator = None;
            }
            continue;
        }

        if let Ok(number) = col_str.trim().parse::<u64>() {
            temp_promblem_numbers.push(number);
        } 

        let op_char = grid[height - 1].get(x).unwrap_or(&' ');
        if *op_char == '+' || *op_char == '*' {
            current_operator = Some(*op_char);
        }


    }

    if !temp_promblem_numbers.is_empty() {
        end_sum += process_group(&mut temp_promblem_numbers, current_operator);
    }

    println!("Part 2: {}", end_sum);

}


fn main() {
    let content = fs::read_to_string("inputs/06/input.txt").expect("file?");

    part1(&content);
    part2(&content);
}