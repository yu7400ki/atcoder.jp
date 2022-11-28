use proconio::{fastout, input};
use std::cmp::min;
use std::collections::HashSet;
use std::i64;

fn solve(s: &Vec<char>, priority: char) -> i64 {
    if s.iter().collect::<HashSet<_>>().len() == 1 {
        return 0;
    }

    let mut res = vec![' '; s.len() - 1];
    for i in 0..s.len() - 1 {
        if s[i] == priority || s[i + 1] == priority {
            res[i] = priority;
        } else {
            res[i] = s[i];
        }
    }

    1 + solve(&res, priority)
}

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let s = s.chars().collect::<Vec<_>>();
    let set = s.iter().collect::<HashSet<_>>();
    let mut ans = i64::MAX;

    for i in 0..set.len() {
        ans = min(ans, solve(&s, **set.iter().nth(i).unwrap()));
    }

    println!("{}", ans);
}
