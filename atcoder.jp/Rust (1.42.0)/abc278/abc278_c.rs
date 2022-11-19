use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        _n: usize,
        q: usize,
    }

    let mut follows: HashSet<(usize, usize)> = HashSet::new();

    for _ in 0..q {
        input! {
            t: usize,
            a: usize,
            b: usize,
        }

        match t {
            1 => {
                follows.insert((a, b));
            }
            2 => {
                follows.remove(&(a, b));
            }
            3 => {
                if follows.contains(&(a, b)) && follows.contains(&(b, a)) {
                    println!("Yes");
                } else {
                    println!("No");
                }
            }
            _ => unreachable!()
        }
    }
}
