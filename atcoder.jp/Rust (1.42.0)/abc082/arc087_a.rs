use proconio::{fastout, input};
use std::cmp::Ordering;

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
        n: usize,
        a: [usize; n],
    }

    let cnt = counter(&a);
    let mut ans = 0;

    for (k, v) in cnt {
        match v.cmp(&k) {
            Ordering::Less => ans += v,
            Ordering::Equal => (),
            Ordering::Greater => ans += v - k,
        }
    }

    println!("{}", ans);
}
