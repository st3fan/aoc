use std::{fs, path::Path};

//

fn read_input_lines<P, T>(path: P, transformer: fn(&str) -> T) -> std::io::Result<Vec<T>>
where
    P: AsRef<Path>,
{
    let mut input: Vec<T> = vec![];
    let contents = fs::read_to_string(path).unwrap();
    for line in contents.lines() {
        input.push(transformer(line));
    }
    Ok(input)
}

//

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Position {
    x: usize,
    y: usize,
}

impl Position {
    fn new(x: usize, y: usize) -> Self {
        Self { x, y }
    }

    fn from_str(s: &str) -> Self {
        let c: Vec<&str> = s.split(',').collect();
        Self {
            x: c[0].parse().unwrap(),
            y: c[1].parse().unwrap(),
        }
    }
}

#[test]
fn position_from_str() {
    assert_eq!(Position::from_str("0,0"), Position { x: 0, y: 0 });
    assert_eq!(Position::from_str("123,456"), Position { x: 123, y: 456 });
    assert_eq!(Position::from_str("999,999"), Position { x: 999, y: 999 });
}

//

struct LightsIterator {
    from: Position,
    to: Position,
    x: usize,
    y: usize,
}

impl LightsIterator {
    fn new(from: Position, to: Position) -> Self {
        Self {
            from,
            to,
            x: from.x,
            y: from.y,
        }
    }
}

impl Iterator for LightsIterator {
    type Item = Position;

    fn next(&mut self) -> Option<Self::Item> {
        if self.y > self.to.y {
            return None;
        }

        let position = Position::new(self.x, self.y);

        self.x += 1;
        if self.x > self.to.x {
            self.x = self.from.x;
            self.y += 1;
        }

        Some(position)
    }
}

//

#[derive(Debug, Eq, PartialEq)]
enum Instruction {
    Toggle { from: Position, to: Position },
    TurnOn { from: Position, to: Position },
    TurnOff { from: Position, to: Position },
}

impl Instruction {
    fn from_str(s: &str) -> Instruction {
        let c: Vec<&str> = s.split(' ').collect();

        if c[0] == "toggle" {
            return Instruction::Toggle {
                from: Position::from_str(c[1]),
                to: Position::from_str(c[3]),
            };
        }

        if c[1] == "on" {
            return Instruction::TurnOn {
                from: Position::from_str(c[2]),
                to: Position::from_str(c[4]),
            };
        }

        if c[1] == "off" {
            return Instruction::TurnOff {
                from: Position::from_str(c[2]),
                to: Position::from_str(c[4]),
            };
        }

        panic!("Unexpected input");
    }

    /// Return an iterator that loops over all the Positions of lights affected by this instruction.
    fn lights(&self) -> LightsIterator {
        match self {
            Instruction::Toggle { from, to } => LightsIterator::new(*from, *to),
            Instruction::TurnOff { from, to } => LightsIterator::new(*from, *to),
            Instruction::TurnOn { from, to } => LightsIterator::new(*from, *to),
        }
    }
}

//

struct Grid {
    lights: Vec<u32>,
}

impl Grid {
    fn new() -> Self {
        Self {
            lights: vec![0; 1_000_000],
        }
    }

    fn toggle(&mut self, position: Position) {
        let i = (position.y * 1000) + position.x;
        self.lights[i] ^= 1;
    }

    fn set(&mut self, position: Position) {
        let i = (position.y * 1000) + position.x;
        self.lights[i] = 1;
    }

    fn clear(&mut self, position: Position) {
        let i = (position.y * 1000) + position.x;
        self.lights[i] = 0;
    }

    fn inc(&mut self, position: Position) {
        let i = (position.y * 1000) + position.x;
        self.lights[i] += 1;
    }

    fn dec(&mut self, position: Position) {
        let i = (position.y * 1000) + position.x;
        if self.lights[i] != 0 {
            self.lights[i] -= 1;
        }
    }

    fn count(&self) -> usize {
        self.lights.iter().filter(|v| **v != 0).count()
    }

    fn total(&self) -> u32 {
        self.lights.iter().sum()
    }
}

//

pub fn part1() -> usize {
    let mut grid = Grid::new();
    for instruction in read_input_lines("input.txt", Instruction::from_str).unwrap() {
        match instruction {
            Instruction::Toggle { from: _, to: _ } => {
                instruction.lights().for_each(|p| grid.toggle(p));
            }
            Instruction::TurnOff { from: _, to: _ } => {
                instruction.lights().for_each(|p| grid.clear(p));
            }
            Instruction::TurnOn { from: _, to: _ } => {
                instruction.lights().for_each(|p| grid.set(p));
            }
        }
    }
    grid.count()
}

pub fn part2() -> u32 {
    let mut grid = Grid::new();
    for instruction in read_input_lines("input.txt", Instruction::from_str).unwrap() {
        match instruction {
            Instruction::Toggle { from: _, to: _ } => {
                for position in instruction.lights() {
                    grid.inc(position);
                    grid.inc(position);
                }
            }
            Instruction::TurnOff { from: _, to: _ } => {
                instruction.lights().for_each(|p| grid.dec(p));
            }
            Instruction::TurnOn { from: _, to: _ } => {
                instruction.lights().for_each(|p| grid.inc(p));
            }
        }
    }
    grid.total()
}

//

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 543903);
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 14687245);
    }
}
