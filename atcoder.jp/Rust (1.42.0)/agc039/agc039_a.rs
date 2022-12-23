use proconio::{fastout, input};
use std::collections::HashSet;

fn split(s: &String) -> Vec<Vec<char>> {
    s.chars().fold(vec![vec![' '; 0]; 1], |mut acc, c| {
        if c == *acc.last().unwrap().last().unwrap_or(&c) {
            acc.last_mut().unwrap().push(c);
        } else {
            acc.push(vec![c]);
        }
        acc
    })
}

#[fastout]
fn main() {
    input! {
        s: String,
        k: usize,
    }

    let ans = {
        if s.chars().collect::<HashSet<_>>().len() == 1 {
            s.len() * k / 2
        } else {
            if s.chars().next().unwrap() == s.chars().last().unwrap() {
                let s = split(&s);
                let a = s.first().unwrap().len();
                let b = s.last().unwrap().len();
                s.iter().fold(0, |acc, v| acc + v.len() / 2) * k
                    - (a / 2 + b / 2 - (a + b) / 2) * (k - 1)
            } else {
                split(&s).iter().fold(0, |acc, v| acc + v.len() / 2) * k
            }
        }
    };

    println!("{}", ans);
}
