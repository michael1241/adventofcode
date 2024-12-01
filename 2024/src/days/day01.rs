use crate::{Solution, SolutionPair};
use std::fs::read_to_string;
use counter::Counter;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let input = read_to_string("input/day01.txt").unwrap();
    let pairs: Vec<_> = input.lines().map(parse_line).collect();
    let (mut col1, mut col2): (Vec<_>, Vec<_>) = pairs.into_iter().unzip();
    col1.sort();
    col2.sort();
    let diffs = col1.iter().zip(col2.iter()).map(|(&x, &y)| (x - y).abs());
    let sol1: i32 = diffs.sum();

    // first list has no duplicates
    let counter2 = col2.iter().collect::<Counter<_>>();
    let sol2: usize = col1.iter().map(|x| (*x as usize) * counter2[x]).sum();

    (Solution::from(sol1), Solution::from(sol2))
}

fn parse_line(line: &str) -> (i32, i32) {
    let (a, b) = line.split_once("   ").unwrap();
    (a.parse::<i32>().unwrap(), b.parse::<i32>().unwrap())
}