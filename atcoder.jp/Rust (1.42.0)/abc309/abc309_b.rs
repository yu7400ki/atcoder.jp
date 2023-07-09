use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [String; n],
    }

    let mut a = a
        .into_iter()
        .map(|s| s.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut outside = VecDeque::new();
    for x in 0..n {
        outside.push_back(a[0][x]);
    }
    for y in 1..n {
        outside.push_back(a[y][n - 1]);
    }
    for x in (0..n - 1).rev() {
        outside.push_back(a[n - 1][x]);
    }
    for y in (1..n - 1).rev() {
        outside.push_back(a[y][0]);
    }
    let last = outside.pop_back().unwrap();
    outside.push_front(last);

    for x in 0..n {
        a[0][x] = outside.pop_front().unwrap();
    }
    for y in 1..n {
        a[y][n - 1] = outside.pop_front().unwrap();
    }
    for x in (0..n - 1).rev() {
        a[n - 1][x] = outside.pop_front().unwrap();
    }
    for y in (1..n - 1).rev() {
        a[y][0] = outside.pop_front().unwrap();
    }

    for y in 0..n {
        println!("{}", a[y].iter().collect::<String>());
    }
}
