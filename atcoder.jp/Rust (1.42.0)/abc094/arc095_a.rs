use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        x: [usize; n],
    }

    let sorted = x.clone().into_iter().sorted().collect::<Vec<_>>();
    let median = sorted[n / 2];

    for i in x {
        if i < median {
            println!("{}", median);
        } else {
            println!("{}", sorted[n / 2 - 1]);
        }
    }
}
