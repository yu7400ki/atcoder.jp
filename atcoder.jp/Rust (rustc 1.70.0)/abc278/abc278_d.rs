use proconio::{fastout, input, marker::Usize1};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [usize; n],
        q: usize,
    }

    let mut a = a.into_iter().enumerate().collect::<HashMap<_, _>>();
    let mut v = 0;

    for _ in 0..q {
        input! {
            t: usize,
        }
        match t {
            1 => {
                input! {
                    x: usize,
                }
                v = x;
                a.clear();
            }
            2 => {
                input! {
                    i: Usize1,
                    x: usize,
                }
                *a.entry(i).or_insert(0) += x;
            }
            3 => {
                input! {
                    i: Usize1,
                }
                println!("{}", a.get(&i).unwrap_or(&0) + v);
            }
            _ => unreachable!(),
        }
    }
}
