use std::fs;

fn read_input() -> Result<String, std::io::Error> {
    fs::read_to_string("input.txt")
}

fn char2increment(c: char) -> i32 {
    match c {
        ')' => -1,
        '(' => 1,
        _ => panic!("Unexpected character in input: {}", c),
    }
}

fn part1(input: &String) -> i32 {
    let mut floor = 0;
    for c in input.chars() {
        floor += char2increment(c);
    }
    floor
}

fn part2(input: &String) -> usize {
    let mut floor = 0;
    for (i, c) in input.chars().enumerate() {
        floor += char2increment(c);
        if floor == -1 {
            return i;
        }
    }
    0
}

fn main() {
    let input = read_input().unwrap();
    println!("Part one: {}", part1(&input));
    println!("Part two: {}", part2(&input));
}
