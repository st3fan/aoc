use regex::Regex;
use std::{collections::HashMap, fs, path::Path};

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

#[derive(Debug, Eq, PartialEq)]
enum Instruction {
    Nop,
    RightShift {
        src: String,
        int: u16,
        dst: String,
    },
    LeftShift {
        src: String,
        int: u16,
        dst: String,
    },
    AndReg {
        src: String,
        reg: String,
        dst: String,
    },
    AndVal {
        val: u16,
        reg: String,
        dst: String,
    },
    OrReg {
        src: String,
        reg: String,
        dst: String,
    },
    OrVal {
        val: u16,
        reg: String,
        dst: String,
    },
    MovReg {
        reg: String,
        dst: String,
    },
    MovVal {
        val: u16,
        dst: String,
    },
    Not {
        reg: String,
        dst: String,
    },
}

fn get_matches(s: &str, re: Regex) -> Option<Vec<String>> {
    if let Some(captures) = re.captures(s) {
        let mut v = Vec::new();
        for i in 1..captures.len() {
            let s = String::from(captures.get(i).unwrap().as_str());
            v.push(s);
        }
        return Some(v);
    }
    None
}

impl Instruction {
    fn from_str(s: &str) -> Instruction {
        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::RightShift {
                src: matches[0].clone(),
                int: matches[1].parse().unwrap(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::LeftShift {
                src: matches[0].clone(),
                int: matches[1].parse().unwrap(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([a-z]+) AND ([a-z]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::AndReg {
                src: matches[0].clone(),
                reg: matches[1].clone(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([0-9]+) AND ([a-z]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::AndVal {
                val: matches[0].parse().unwrap(),
                reg: matches[1].clone(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([a-z]+) OR ([a-z]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::OrReg {
                src: matches[0].clone(),
                reg: matches[1].clone(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(
            s,
            Regex::new(r"^([0-9]+) OR ([a-z]+) -> ([a-z]+)$").unwrap(),
        ) {
            return Instruction::OrVal {
                val: matches[0].parse().unwrap(),
                reg: matches[1].clone(),
                dst: matches[2].clone(),
            };
        }

        if let Some(matches) = get_matches(s, Regex::new(r"^([a-z]+) -> ([a-z]+)$").unwrap()) {
            return Instruction::MovReg {
                reg: matches[0].clone(),
                dst: matches[1].clone(),
            };
        }

        if let Some(matches) = get_matches(s, Regex::new(r"^([0-9]+) -> ([a-z]+)$").unwrap()) {
            return Instruction::MovVal {
                val: matches[0].parse().unwrap(),
                dst: matches[1].clone(),
            };
        }

        if let Some(matches) = get_matches(s, Regex::new(r"^NOT ([a-z]+) -> ([a-z]+)$").unwrap()) {
            return Instruction::Not {
                reg: matches[0].clone(),
                dst: matches[1].clone(),
            };
        }

        panic!("Unknown instruction: {}", s);
    }
}

#[test]
fn test_parse_rshift() {
    assert_eq!(
        Instruction::from_str("aa RSHIFT 5 -> bb"),
        Instruction::RightShift {
            src: "aa".to_string(),
            int: 5,
            dst: "bb".to_string()
        }
    );
}

#[test]
fn test_parse_lshift() {
    assert_eq!(
        Instruction::from_str("aa LSHIFT 5 -> bb"),
        Instruction::LeftShift {
            src: "aa".to_string(),
            int: 5,
            dst: "bb".to_string()
        }
    );
}

#[test]
fn test_and_reg() {
    assert_eq!(
        Instruction::from_str("a AND b -> c"),
        Instruction::AndReg {
            src: "a".to_string(),
            reg: "b".to_string(),
            dst: "c".to_string()
        }
    );
}

#[test]
fn test_and_val() {
    assert_eq!(
        Instruction::from_str("7 AND b -> c"),
        Instruction::AndVal {
            val: 7,
            reg: "b".to_string(),
            dst: "c".to_string()
        }
    );
}

#[test]
fn test_or_reg() {
    assert_eq!(
        Instruction::from_str("a OR b -> c"),
        Instruction::OrReg {
            src: "a".to_string(),
            reg: "b".to_string(),
            dst: "c".to_string()
        }
    );
}

#[test]
fn test_or_val() {
    assert_eq!(
        Instruction::from_str("7 OR b -> c"),
        Instruction::OrVal {
            val: 7,
            reg: "b".to_string(),
            dst: "c".to_string()
        }
    );
}

#[test]
fn test_mov_val() {
    assert_eq!(
        Instruction::from_str("123 -> abc"),
        Instruction::MovVal {
            val: 123,
            dst: "abc".to_string()
        }
    );
}

#[test]
fn test_mov_reg() {
    assert_eq!(
        Instruction::from_str("xyz -> abc"),
        Instruction::MovReg {
            reg: "xyz".to_string(),
            dst: "abc".to_string()
        }
    );
}

#[test]
fn test_parse_not() {
    assert_eq!(
        Instruction::from_str("NOT aaa -> bbb"),
        Instruction::Not {
            reg: "aaa".to_string(),
            dst: "bbb".to_string()
        }
    );
}

//

fn execute(instruction: &Instruction, registers: &mut HashMap<String, u16>) -> bool {
    // println!("Executing {:?}", instruction);
    match instruction {
        Instruction::RightShift { src, int, dst } => {
            if let Some(src) = registers.get(src) {
                registers.insert(dst.clone(), src >> int);
                return true;
            }
        }

        Instruction::LeftShift { src, int, dst } => {
            if let Some(src) = registers.get(src) {
                registers.insert(dst.clone(), src << int);
                return true;
            }
        }

        Instruction::AndReg { src, reg, dst } => {
            if let Some(src) = registers.get(src) {
                if let Some(reg) = registers.get(reg) {
                    registers.insert(dst.clone(), src & reg);
                    return true;
                }
            }
        }

        Instruction::AndVal { val, reg, dst } => {
            if let Some(reg) = registers.get(reg) {
                registers.insert(dst.clone(), reg & val);
                return true;
            }
        }

        Instruction::OrReg { src, reg, dst } => {
            if let Some(src) = registers.get(src) {
                if let Some(reg) = registers.get(reg) {
                    registers.insert(dst.clone(), src | reg);
                    return true;
                }
            }
        }

        Instruction::OrVal { val, reg, dst } => {
            if let Some(reg) = registers.get(reg) {
                registers.insert(dst.clone(), reg | val);
                return true;
            }
        }

        Instruction::Not { reg, dst } => {
            if let Some(reg) = registers.get(reg) {
                registers.insert(dst.clone(), !reg);
                return true;
            }
        }

        Instruction::MovReg { reg, dst } => {
            if let Some(reg) = registers.get(reg) {
                registers.insert(dst.clone(), *reg);
                return true;
            }
        }

        Instruction::MovVal { val, dst } => {
            if !registers.contains_key(dst) {
                registers.insert(dst.clone(), *val);
            }
            return true;
        }

        Instruction::Nop => {}
    }

    false
}

//

fn all_nops(instructions: &Vec<Instruction>) -> bool {
    instructions.iter().all(|i| matches!(i, Instruction::Nop))
}

//

pub fn part1() -> u16 {
    let mut registers: HashMap<String, u16> = HashMap::new();
    let mut instructions = read_input_lines("input.txt", Instruction::from_str).unwrap();

    while !all_nops(&instructions) {
        for instruction in instructions.iter_mut() {
            if execute(instruction, &mut registers) {
                *instruction = Instruction::Nop;
            }
        }
    }

    *registers.get("a").unwrap()
}

pub fn part2() -> u16 {
    let mut registers: HashMap<String, u16> = HashMap::new();
    let mut instructions = read_input_lines("input.txt", Instruction::from_str).unwrap();

    registers.insert("b".to_string(), part1());

    while !all_nops(&instructions) {
        for instruction in instructions.iter_mut() {
            if execute(instruction, &mut registers) {
                *instruction = Instruction::Nop;
            }
        }
    }

    *registers.get("a").unwrap()
}

//

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 46065);
    }
    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 14134);
    }
}
