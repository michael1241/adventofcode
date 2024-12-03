use crate::{Solution, SolutionPair};
use std::fs::read_to_string;
use regex::Regex;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let input = read_to_string("input/day03.txt").unwrap();
    let re = Regex::new(r"mul\(([\d]{1,3}),([\d]{1,3})\)|(do\(\))()|(don\'t\(\))()").unwrap();

    let mut sol1: u64 = 0;
    let mut sol2: u64 = 0;
    let mut doing: u64 = 1;

    for (_, [a, b]) in re.captures_iter(&input).map(|x| x.extract()) {

        let (val1, val2, doing) = match (a, b) {
            ("do()", "") => (0, 0, 1),
            ("don't()", "") => (0, 0, 0),
            (i1, i2) => (i1.parse::<u64>().unwrap(), i2.parse::<u64>().unwrap(), doing),
        };
        println!("{:?}", doing);
        let (mut add1, mut add2) = update_sols(val1, val2, &doing);
        sol1 = sol1 + add1;
        sol2 = sol2 + add2;
    }


    fn update_sols(a: u64, b: u64, doing: &u64) -> (u64, u64) {
        let value: u64 = a * b;
        if *doing == 1 {
            (value, value)
        } else {
            (value, 0)
        }
    }


    (Solution::from(sol1), Solution::from(sol2))
}
