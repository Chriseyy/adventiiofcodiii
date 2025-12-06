use std::fs;


fn check_range(range: &Vec<(u64, u64)>, ingredient: u64) -> bool {
    for r in range {
        if ingredient >= r.0 && ingredient <= r.1 {
            return true;
        }
    }
    false
}

fn part1(content: &str) {
    let mut fresh_ingredients: u32 = 0;
    let mut fresh_ranges = Vec::new();
    let mut ingredient_ids = Vec::new();
    
    let content_split: Vec<&str> = content.split("\n").collect();
    let space_idx = content_split.iter().position(|&r| r=="").unwrap();
    
    for pairs in &content_split[0..space_idx] {
        let pairs_split: Vec<&str> = pairs.split("-").collect();
        fresh_ranges.push((pairs_split[0].parse::<u64>().unwrap(), pairs_split[1].parse::<u64>().unwrap()));
        }

    for ingredient in &content_split[space_idx+1..] {
        ingredient_ids.push(ingredient.parse::<u64>().unwrap());
    }

    for ingredient in ingredient_ids {
        if check_range(&fresh_ranges, ingredient) {
            fresh_ingredients += 1;
        }
    }

    println!("Part 1: {}", fresh_ingredients);

}



fn part2(content: &str) {
    let mut fresh_ranges = Vec::new();
    
    let content_split: Vec<&str> = content.split("\n").collect();
    let space_idx = content_split.iter().position(|&r| r=="").unwrap();

    for pairs in &content_split[0..space_idx] {
        let parts: Vec<&str> = pairs.split('-').collect();
        let start = parts[0].parse::<u64>().unwrap();
        let end = parts[1].parse::<u64>().unwrap();
        fresh_ranges.push((start, end));
    }

    fresh_ranges.sort_by_key(|k| k.0);    // python: fresh_ranges.sort(key=lambda x: x[0])

    let mut merged_ranges: Vec<(u64, u64)> = Vec::new();

    if !fresh_ranges.is_empty() {
        //start
        let (mut cur_start, mut cur_end) = fresh_ranges[0];

        for &(next_start, next_end) in fresh_ranges.iter().skip(1) {
            
            if next_start <= cur_end + 1 {
                cur_end = cur_end.max(next_end);
            } else {
                merged_ranges.push((cur_start, cur_end));
                cur_start = next_start;
                cur_end = next_end;
            }
        }
        // paaaarrrree mergen :D 
        merged_ranges.push((cur_start, cur_end));
    }

    // zählii
    let mut all_ranges_count: u64 = 0;
    for (start, end) in merged_ranges {
        all_ranges_count += end - start + 1;
    }

    println!("Part 2: {}", all_ranges_count);
}


fn main() {
    let content = fs::read_to_string("inputs/05/input.txt").expect("file?");

    part1(&content);
    part2(&content);
}