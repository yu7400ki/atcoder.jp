use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
    }

    let s = s
        .iter()
        .map(|s| {
            s.chars()
                .enumerate()
                .filter(|(_, c)| *c == 'o')
                .map(|(i, _)| i)
                .collect::<HashSet<_>>()
        })
        .collect::<Vec<_>>();

    let mut ans = 0;
    for i in 0..n {
        for j in i+1..n {
            if s[i].union(&s[j]).count() == m {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
