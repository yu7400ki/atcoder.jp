use proconio::{fastout, input};
use std::collections::HashMap;

fn combination(n: i64, r: i64) -> i64 {
    let mut res = 1;
    for i in 0..r {
        res *= n - i;
        res /= i + 1;
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let counter = a.iter().fold(HashMap::new(), |mut acc: HashMap<i64, i64>, &x| {
        *acc.entry(x).or_insert(0) += 1;
        acc
    });

    let mut comb = HashMap::new();

    for (&i, &v) in counter.iter() {
        comb.insert(i, combination(v, 2));
    }

    let cnt = comb.values().sum::<i64>();

    for i in a.iter() {
        let ans = cnt - comb[i] + combination(counter[i] - 1, 2);
        println!("{}", ans);
    }
}
