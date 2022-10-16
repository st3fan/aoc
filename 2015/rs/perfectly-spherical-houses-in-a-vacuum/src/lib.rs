use std::collections::HashMap;
use std::fs;

enum Direction {
    North,
    East,
    South,
    West
}

//

#[derive(Clone, Eq, PartialEq, Hash)]
struct Position {
    x: i32,
    y: i32
}

impl Position {
    fn zero() -> Self {
        Position { x: 0, y: 0 }
    }
}

//

struct Santa {
    position: Position,
}

impl Santa {
    fn new() -> Self {
        Santa { position: Position::zero() }
    }

    fn north(&mut self) {
        self.position.y += 1;
    }

    fn east(&mut self) {
        self.position.x += 1;
    }

    fn south(&mut self) {
        self.position.y -= 1;
    }

    fn west(&mut self) {
        self.position.x -= 1;
    }

    fn mov(&mut self, direction: Direction) {
        match direction {
            Direction::North => self.north(),
            Direction::East  => self.east(),
            Direction::South => self.south(),
            Direction::West  => self.west()
        }
    }
}

//

struct InfiniteGrid<T> {
    nodes: HashMap<Position, T>,
}

impl<T> InfiniteGrid<T> {
    fn new() -> Self {
        Self { nodes: HashMap::new() }
    }

    fn set(&mut self, position: Position, value: T) {
        self.nodes.insert(position, value);
    }
}

//

fn read_input() -> Vec<Direction> {
   let mut result: Vec<Direction> = vec![];
   for c in fs::read_to_string("input.txt").unwrap().chars() {
      result.push(match c {
          '^' => Direction::North,
          '>' => Direction::East,
          'v' => Direction::South,
          '<' => Direction::West,
          _ => panic!("Unexpected character in input: {}", c)
      })
   }
   result
}

//

pub fn part1() -> usize {
    let mut grid: InfiniteGrid<bool> = InfiniteGrid::new();
    let mut santa = Santa::new();

    grid.set(Position::zero(), true);

    for direction in read_input() {
        santa.mov(direction);
        grid.set(santa.position.clone(), true);
    }

    grid.nodes.len()
}

pub fn part2() -> usize {
    let mut grid: InfiniteGrid<bool> = InfiniteGrid::new();
    let mut santas = [Santa::new(), Santa::new()];

    grid.set(Position::zero(), true);

    let mut i = 0;

    for direction in read_input() {
        santas[i].mov(direction);
        grid.set(santas[i].position.clone(), true);
        i = i ^ 1
    }

    grid.nodes.len()
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 2572);
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 2631);
    }
}
