use proconio::{fastout, input};
use std::collections::BTreeMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [isize; n],
    }

    let map = a.into_iter().fold(BTreeMap::new(), |mut p, c| {
        *p.entry(c).or_insert(0) += 1;
        p
    });

    for (_k, v) in map.iter().rev() {
        println!("{}", v)
    }
    for _ in 0..(n - map.len()) {
        println!("0")
    }
}
