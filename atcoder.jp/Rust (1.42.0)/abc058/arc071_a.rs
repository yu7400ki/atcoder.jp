use proconio::{fastout, input};
use std::collections::BTreeSet;

fn counter<T>(v: &[T]) -> std::collections::HashMap<T, usize>
where
    T: std::cmp::Eq + std::hash::Hash + Copy,
{
    v.iter()
        .fold(std::collections::HashMap::new(), |mut acc, &x| {
            *acc.entry(x).or_insert(0) += 1;
            acc
        })
}

#[fastout]
fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let s_char = s
        .iter()
        .map(|s| s.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let s_count = s_char.iter().map(|s| counter(s)).collect::<Vec<_>>();

    let s_intersection = s_count
        .iter()
        .map(|s| s.keys().collect::<BTreeSet<_>>())
        .fold(s_count[0].keys().collect::<BTreeSet<_>>(), |acc, x| {
            acc.intersection(&x).copied().collect()
        });

    let ans = s_intersection.iter().fold("".to_string(), |acc, x| {
        acc + &x.to_string().repeat(s_count.iter().min_by_key(|s| s[x]).unwrap()[x])
    });

    if ans.len() > 0 {
        println!("{}", ans);
    }
}
