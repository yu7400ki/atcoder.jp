use proconio::{fastout, input};

const MOD: usize = 998_244_353;

#[fastout]
fn main() {
    input! {
        n: usize,
        d: [usize; n],
    }

    let d_count = counter(&d);

    if d[0] != 0 || d_count.get(&0).unwrap() != &1 {
        println!("0");
        return;
    }

    let ans = (0..*d.iter().max().unwrap()).fold(1, |acc, i| {
        acc * d_count
            .get(&i)
            .unwrap_or(&0)
            .pow(*d_count.get(&(i + 1)).unwrap_or(&0) as u32)
            % MOD
    });

    println!("{}", ans);
}

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
