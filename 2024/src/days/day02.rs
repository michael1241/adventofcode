use crate::{Solution, SolutionPair};
use std::fs::read_to_string;
use itertools::Itertools;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let input = read_to_string("input/day02.txt").unwrap();
    let reports: Vec<_> = input.lines().map(parse_line).collect();
    let all_diffs: Vec<Vec<i32>> = reports.clone().into_iter().map(get_pair_diffs).collect();
    let passing_part_1: Vec<_> = all_diffs.clone().into_iter().filter(same_sign).filter(max_abs_diff_allowed).collect();
    let sol1: u64 = passing_part_1.len().try_into().unwrap();

    let mut sol2: u64 = 0;
    let report_possibles: Vec<Vec<Vec<i32>>> = reports.clone().into_iter().map(possible_reports).collect();
    for report_set in report_possibles {
        let report_set_diffs: Vec<Vec<i32>> = report_set.clone().into_iter().map(get_pair_diffs).collect();
        let report_set_passing: Vec<_> = report_set_diffs.clone().into_iter().filter(same_sign).filter(max_abs_diff_allowed).collect();
        if !report_set_passing.is_empty() {sol2 += 1}
    }

    (Solution::from(sol1), Solution::from(sol2))
}

fn parse_line(line: &str) -> Vec<i32> {
    let levels: Vec<i32> = line.split_whitespace().filter_map(|x| x.parse().ok()).collect();
    levels
}

fn get_pair_diffs(report: Vec<i32>) -> Vec<i32> {
    report.into_iter().tuple_windows().map(|(a, b)| a - b).collect()
}

fn same_sign(pair_diffs: &Vec<i32>) -> bool {
    pair_diffs.iter().all(|x| *x > 0) || pair_diffs.iter().all(|x| *x < 0)
}

fn max_abs_diff_allowed(pair_diffs: &Vec<i32>) -> bool {
    let max_abs_diff: i32 = pair_diffs.iter().map(|x| (*x).abs()).max().expect("I don't know");
    max_abs_diff >= 1 && max_abs_diff <= 3
}

fn possible_reports(report: Vec<i32>) -> Vec<Vec<i32>> {
    let mut possibles: Vec<Vec<i32>> = vec![report.clone()];
    for (index, element) in report.clone().into_iter().enumerate() {
        let mut adjusted = report.clone();
        adjusted.remove(index);
        possibles.push(adjusted);
    }
    return possibles
}

