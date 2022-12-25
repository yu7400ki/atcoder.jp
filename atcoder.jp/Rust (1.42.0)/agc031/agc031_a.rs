use proconio::{fastout, input};

const MOD: usize = 1_000_000_007;

fn counter<T>(v: &[T]) -> std::collections::HashMap<T, usize>
where
    T: std::cmp::Eq + std::hash::Hash + Copy,
{
    v.iter()
        .fold(std::collections::HashMap::new(), |mut map, &x| {
            *map.entry(x).or_insert(0) += 1;
            map
        })
}

#[fastout]
fn main() {
    input! {
        _n: usize,
        s: String,
    }

    let count = counter(&s.chars().collect::<Vec<char>>());

    let ans = count
        .into_iter()
        .fold(1, |acc, (_, v)| (acc * (v + 1)) % MOD)
        - 1;

    println!("{}", ans);
}
