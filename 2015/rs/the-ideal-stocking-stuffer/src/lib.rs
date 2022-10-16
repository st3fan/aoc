use md5;

const INPUT: &str = "bgvyzdsv";

pub fn part1() -> usize {
    for i in 0..999999999 {
        let digest = md5::compute(format!("{}{}", INPUT, i));
        if digest[0] == 0 && digest[1] == 0 && digest[2] & 0xf0 == 0 {
            return i;
        }
    }
    0
}

pub fn part2() -> usize {
    for i in 0..999999999 {
        let digest = md5::compute(format!("{}{}", INPUT, i));
        if digest[0] == 0 && digest[1] == 0 && digest[2] == 0 {
            return i;
        }
    }
    0
}

//

#[cfg(test)]
mod tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 254575);
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 1038736);
    }
}
