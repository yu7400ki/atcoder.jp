use proconio::{fastout, input};

fn counter<T>(v: &[T]) -> std::collections::BTreeMap<T, usize>
where
    T: std::cmp::Eq + std::hash::Hash + Clone + std::cmp::Ord,
{
    v.iter()
        .fold(std::collections::BTreeMap::new(), |mut map, x| {
            *map.entry(x.clone()).or_insert(0) += 1;
            map
        })
}

fn combination(n: usize, r: usize) -> usize {
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
        s: [String; n],
    }

    let map = s
        .iter()
        .map(|s| s.chars().collect::<Vec<_>>())
        .map(|v| counter(&v))
        .map(|v| {
            v.iter()
                .map(|(&k, &v)| (k, v))
                .collect::<Vec<(char, usize)>>()
        })
        .collect::<Vec<_>>();

    let cnt = counter(&map);
    let cnt = cnt
        .values()
        .filter(|&&v| v >= 2)
        .map(|&v| combination(v, 2))
        .sum::<usize>();

    println!("{:?}", cnt);
}
