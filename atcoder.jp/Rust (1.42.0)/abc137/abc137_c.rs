use proconio::{fastout, input};
use std::collections::HashMap;

fn cmb(n: usize, r: usize) -> usize {
    if n < r {
        return 0;
    }
    let mut ans = 1;
    for i in 0..r {
        ans *= n - i;
        ans /= i + 1;
    }
    ans
}

#[fastout]
fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let s: Vec<String> = s
        .into_iter()
        .map(|s| {
            let mut s = s.chars().collect::<Vec<char>>();
            s.sort_by(|a, b| b.cmp(a));
            s.iter().collect::<String>()
        })
        .collect::<Vec<String>>();

    let count = s.iter().fold(HashMap::new(), |mut c, p| {
        *c.entry(p).or_insert(0) += 1;
        c
    });

    let ans = count.iter().fold(0, |c, p| c + cmb(*p.1, 2));

    println!("{}", ans);
}
