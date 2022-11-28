use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        d: [i64; n],
        m: usize,
        t: [i64; m],
    }

    let d_cnt = d.iter().fold(HashMap::new(), |mut acc, &x| {
        *acc.entry(x).or_insert(0) += 1;
        acc
    });

    let t_cnt = t.iter().fold(HashMap::new(), |mut acc, &x| {
        *acc.entry(x).or_insert(0) += 1;
        acc
    });

    let ans = t_cnt.iter().all(|(&k, &v)| d_cnt.get(&k).unwrap_or(&0) >= &v);

    println!("{}", if ans { "YES" } else { "NO" });
}
