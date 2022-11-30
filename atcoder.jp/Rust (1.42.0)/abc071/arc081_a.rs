use proconio::{fastout, input};
use std::collections::BTreeMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let counter = a.iter().fold(BTreeMap::new(), |mut acc, &x| {
        *acc.entry(x).or_insert(0) += 1;
        acc
    });

    let filtered = counter
        .iter()
        .filter(|(_, &v)| v >= 2)
        .rev()
        .collect::<Vec<_>>();
    
    if filtered.len() < 2 {
        println!("0");
    } else if filtered[0].1 >= &4 {
        println!("{}", filtered[0].0 * filtered[0].0);
    } else {
        println!("{}", filtered[0].0 * filtered[1].0);
    }
}
