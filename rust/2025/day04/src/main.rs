use std::fs;

fn check_field(grid: &[Vec<char>], row: usize, col: usize) -> bool {
    let directions: [(isize, isize); 8] = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1),];

    if grid[row][col] == '@' {
        let mut neighbors = 0;
        let height = grid.len() as isize;
        let width = grid[0].len() as isize;

        for (dr, dc) in directions {
            let new_row = row as isize + dr;
            let new_col = col as isize + dc;

            if new_row >= 0 && new_row < height && new_col >= 0 && new_col < width {
                if grid[new_row as usize][new_col as usize] == '@' {
                    neighbors += 1;
                }
            }
        }

        if neighbors < 4 {
            return true;
        }
    }

    false
}

// beides geht was besser kp 
// fn part1(grid: &[Vec<char>]) {
fn part1(grid: &Vec<Vec<char>>) {
    let mut forklift_accessible = 0;
    for (idx_row, row) in grid.iter().enumerate() {
            for (idx_col, _val) in row.iter().enumerate() {
                if check_field(&grid, idx_row, idx_col) {
                    forklift_accessible += 1;
            }
        }
    }
    println!("Part 1: {}", forklift_accessible);
}

fn part2(grid: &mut Vec<Vec<char>>) { 
    let mut forklift_accessible = 0;

    loop {
        let mut update_list: Vec<(usize, usize)> = Vec::new();

        for (idx_row, row) in grid.iter().enumerate() {
            for (idx_col, _) in row.iter().enumerate() {
                if check_field(grid, idx_row, idx_col) {
                    update_list.push((idx_row, idx_col));
                }
            }
        }

        if update_list.is_empty() {
            break;
        }

        forklift_accessible += update_list.len();

        for (r, c) in update_list {
            grid[r][c] = '.';
        }
    }

    println!("Part 2: {}", forklift_accessible);
}


fn main() {
    let content = fs::read_to_string("inputs/04/input.txt").expect("file?");
    let mut grid: Vec<Vec<char>> = content.lines().map(|line| line.chars().collect()).collect();

    if grid.is_empty() {
        return;
    }

    part1(&grid);
    part2(&mut grid);
}