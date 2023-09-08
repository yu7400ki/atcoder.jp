use proconio::{input, fastout};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut set = (1..=n).collect::<HashSet<usize>>();

    for _ in 0..m {
        input! {
            _: usize,
            b: usize,
        }

        set.remove(&b);
    }

    let ans = if set.len() == 1 {
        set.iter().next().unwrap().to_string()
    } else {
        "-1".to_string()
    };

    println!("{}", ans);
}
