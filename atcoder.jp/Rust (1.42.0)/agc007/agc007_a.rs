use proconio::{fastout, input};

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
        h: usize,
        w: usize,
        a: [String; h],
    }

    let a = a.iter().flat_map(|s| s.chars()).collect::<Vec<_>>();
    let cnt = counter(&a);
    let ans = *cnt.get(&'#').unwrap() == h + w - 1;

    println!("{}", if ans { "Possible" } else { "Impossible" });
}
