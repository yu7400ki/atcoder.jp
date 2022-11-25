use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut set = HashSet::new();

    for n in a {
        if set.contains(&n) {
            set.remove(&n);
        } else {
            set.insert(n);
        }
    }

    println!("{}", set.len());
}
