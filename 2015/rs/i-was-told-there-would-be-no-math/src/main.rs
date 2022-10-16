use std::fs;

#[derive(Debug, PartialEq)]
struct Dimensions {
    length: i32,
    width: i32,
    height: i32,
}

impl Dimensions {
    fn from_str(s: &str) -> Self {
        let components: Vec<&str> = s.split('x').collect();
        Dimensions {
            length: components[0].parse().unwrap(),
            width: components[1].parse().unwrap(),
            height: components[2].parse().unwrap(),
        }
    }

    fn new(length: i32, width: i32, height: i32) -> Self {
        Dimensions {
            length,
            width,
            height,
        }
    }

    fn paper_needed(&self) -> i32 {
        let sides: [i32; 3] = [
            self.length * self.width,
            self.width * self.height,
            self.height * self.length,
        ];
        let a: i32 = sides.iter().sum();
        let b: i32 = *sides.iter().min().unwrap();
        a * 2 + b
    }

    fn ribbon_needed(&self) -> i32 {
        let mut sides: [i32; 3] = [self.length, self.width, self.height];
        sides.sort();
        sides[0] * 2 + sides[1] * 2 + (self.length * self.width * self.height)
    }
}

#[test]
fn test_dimension_from_string() {
    assert_eq!(Dimensions::from_str("2x3x4"), Dimensions::new(2, 3, 4));
}

#[test]
fn test_paper_needed() {
    assert_eq!(Dimensions::new(2, 3, 4).paper_needed(), 58);
}

fn read_input() -> Vec<Dimensions> {
    let mut results = Vec::new();
    let contents = fs::read_to_string("input.txt").unwrap();
    for line in contents.lines() {
        results.push(Dimensions::from_str(line));
    }
    results
}

//

fn part1() -> i32 {
    let mut total: i32 = 0;
    for dimension in read_input() {
        total += dimension.paper_needed();
    }
    total
}

fn part2() -> i32 {
    let mut total: i32 = 0;
    for dimension in read_input() {
        total += dimension.ribbon_needed();
    }
    total
}

//

fn main() {
    println!("Part one: {}", part1());
    println!("Part two: {}", part2());
}
