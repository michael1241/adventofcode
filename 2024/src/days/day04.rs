use itertools::Itertools;
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;
use diagonal::{straight_x, straight_y, diagonal_pos_pos, diagonal_pos_neg};

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let grid: Vec<Vec<char>> = read_to_string("input/day04.txt").expect("idk").lines().map(|s| s.chars().collect()).collect();

    let sol1: u64 = make_paths(&grid).into_iter().map(|x| count_matches(x)).collect::<Vec<_>>().iter().sum::<u64>();
    let sol2: u64 = 0;

    (Solution::from(sol1), Solution::from(sol2))
}

fn make_paths(g: &Vec<Vec<char>>) -> Vec<Vec<&char>> {
    [straight_x(g), straight_y(g), diagonal_pos_neg(g), diagonal_pos_pos(g)].concat()
}

fn count_matches(path: Vec<&char>) -> u64 {
    let mut total: u64 = 0;
    for view in path.into_iter().tuple_windows::<(_, _, _, _)>() {
        match view {
            ('X', 'M', 'A', 'S') => *&mut total += 1,
            ('S', 'A', 'M', 'X') => *&mut total += 1,
            _ => ()
        };
    }
    return total
}