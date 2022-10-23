// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

use itertools::Itertools;

//

const PUZZLE_INPUT: [usize; 10] = [1, 1, 1, 3, 1, 2, 2, 1, 1, 3];

//

pub fn turn(input: Vec<usize>) -> Vec<usize> {
    let mut result: Vec<usize> = Vec::new();
    for (key, group) in &input.into_iter().group_by(|e| *e) {
        result.push(group.count());
        result.push(key);
    }
    result
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(super::turn(vec![1]), [1, 1]);
        assert_eq!(super::turn(vec![1, 1]), [2, 1]);
        assert_eq!(super::turn(vec![2, 1]), [1, 2, 1, 1]);
        assert_eq!(super::turn(vec![1, 2, 1, 1]), [1, 1, 1, 2, 2, 1]);
    }
}

//

pub fn part1() -> usize {
    let mut result: Vec<usize> = PUZZLE_INPUT.to_vec();
    for _ in 0..40 {
        result = turn(result);
    }
    result.len()
}

pub fn part2() -> usize {
    let mut result: Vec<usize> = PUZZLE_INPUT.to_vec();
    for _ in 0..50 {
        result = turn(result);
    }
    result.len()
}

#[cfg(test)]
mod puzzle_tests {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 360154);
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 5103798);
    }
}
