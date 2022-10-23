//

use itertools::Itertools;

pub fn is_increasing(s: &String) -> bool {
    for (a, b) in s.chars().tuple_windows() {
        if a >= b {
            return false;
        }
    }
    return true;
}

#[test]
fn test_is_increasing() {
    assert_eq!(is_increasing(&"abc".to_string()), true);
    assert_eq!(is_increasing(&"ace".to_string()), true);
    assert_eq!(is_increasing(&"cba".to_string()), false);
    assert_eq!(is_increasing(&"aab".to_string()), false);
    assert_eq!(is_increasing(&"abb".to_string()), false);
}

//

fn has_increasing_straight(s: &String) -> bool {
    for (a, b, c) in s.chars().tuple_windows() {
        if c as usize == (b as usize + 1) && b as usize == (a as usize + 1) {
            return true;
        }
    }
    false
}

#[test]
fn test_has_increasing_straight() {
    assert_eq!(has_increasing_straight(&"xabcy".to_string()), true);
    assert_eq!(has_increasing_straight(&"abduvx".to_string()), false);
}

//

fn has_unique_pairs(_s: &String) -> bool {
    true
}

//

pub fn part1() -> String {
    "".to_string()
}

pub fn part2() -> String {
    "".to_string()
}

//

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), "vzbxxyzz");
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), "vzcaabcc");
    }
}
