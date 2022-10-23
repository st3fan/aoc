// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

use serde_json::Value;
use std::fs;

//

fn collect_numbers1(value: &Value) -> i64 {
    match value {
        Value::Number(n) => return n.as_i64().unwrap(),
        Value::Array(a) => {
            let mut total: i64 = 0;
            for v in a {
                total += collect_numbers1(&v);
            }
            return total;
        }
        Value::Object(o) => {
            let mut total: i64 = 0;
            for v in o.values() {
                total += collect_numbers1(v);
            }
            return total;
        }
        _ => 0,
    }
}

fn collect_numbers2(value: &Value) -> i64 {
    match value {
        Value::Number(n) => return n.as_i64().unwrap(),
        Value::Array(a) => {
            let mut total: i64 = 0;
            for v in a {
                total += collect_numbers2(&v);
            }
            return total;
        }
        Value::Object(o) => {
            let mut total: i64 = 0;
            for v in o.values() {
                if let Value::String(value) = v {
                    if value == "red" {
                        return 0;
                    }
                }
                total += collect_numbers2(v);
            }
            return total;
        }
        _ => 0,
    }
}

pub fn part1() -> i64 {
    let input = fs::read_to_string("input.json").unwrap();
    let document: Value = serde_json::from_str(input.as_str()).unwrap();
    collect_numbers1(&document)
}

pub fn part2() -> i64 {
    let input = fs::read_to_string("input.json").unwrap();
    let document: Value = serde_json::from_str(input.as_str()).unwrap();
    collect_numbers2(&document)
}

//

#[cfg(test)]
mod advent_of_code {
    #[test]
    fn test_part1() {
        assert_eq!(super::part1(), 119433);
    }

    #[test]
    fn test_part2() {
        assert_eq!(super::part2(), 68466);
    }
}
