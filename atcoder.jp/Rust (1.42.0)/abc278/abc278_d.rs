use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [u64; n],
        q: usize,
    }

    let mut b: Option<u64> = None;
    let mut add: HashMap<usize, u64> = HashMap::new();

    for _ in 0..q {
        input! {
            query: usize,
        }

        match query {
            1 => {
                input! {
                    x: u64,
                }
                b = Some(x);
                add.clear();
            }
            2 => {
                input! {
                    i: usize,
                    x: u64,
                }
                *add.entry(i).or_insert(0) += x;
            }
            _ => {
                input! {
                    i: usize,
                }
                println!("{}", *add.entry(i).or_insert(0) + b.unwrap_or(a[i - 1]));
            }
        }
    }
}
