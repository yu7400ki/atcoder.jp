use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        n: usize,
        c: i64,
        k: i64,
        mut t: [i64; n],
    }

    t.sort();
    let mut t = t.into_iter().collect::<VecDeque<_>>();
    let mut ans = 0;

    while t.len() > 0 {
        let head = t.pop_front().unwrap();
        for _ in 0..c - 1 {
            if t.len() == 0 {
                break;
            }
            if t[0] > head + k {
                break;
            }
            t.pop_front();
        }
        ans += 1;
    }

    println!("{}", ans);
}
