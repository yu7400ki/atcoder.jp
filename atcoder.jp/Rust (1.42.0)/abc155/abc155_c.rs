use proconio::{fastout, input};
use std::collections::BTreeMap;


#[fastout]
fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let counter = s.iter().fold(BTreeMap::new(), |mut acc, x| {
        *acc.entry(x).or_insert(0) += 1;
        acc
    });

    let max = *counter.values().last().unwrap();

    for (k, _) in counter.iter().filter(|(_, v)| **v == max) {
        println!("{}", k);
    }
}
