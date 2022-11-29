use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut ans: VecDeque<i64> = VecDeque::new();
    for i in 0..n {
        if i % 2 == 0 {
            ans.push_back(a[i]);
        } else {
            ans.push_front(a[i]);
        }
    }

    if n % 2 == 1 {
        ans = ans.into_iter().rev().collect();
    }

    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
