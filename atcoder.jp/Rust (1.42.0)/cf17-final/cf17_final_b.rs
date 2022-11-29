use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut counter = HashMap::new();
    counter.insert('a', 0);
    counter.insert('b', 0);
    counter.insert('c', 0);
    let counter = s.chars().fold(counter, |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        acc
    });

    let (c, cnt) = counter
        .iter()
        .max_by_key(|(_, &v)| v)
        .map(|(&k, &v)| (k, v))
        .unwrap();
    
    let rest = counter.iter().filter(|(&k, _)| k != c).map(|(_, &v)| v).collect::<Vec<_>>();

    let ans = rest.iter().all(|&v| v >= cnt - 1);

    println!("{}", if ans { "YES" } else { "NO" });
}
