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
        n: usize,
        v: [usize; n],
    }

    let cnt = counter(&v);
    if cnt.len() == 1 {
        println!("{}", n / 2);
        return;
    }

    let (a, b): (Vec<_>, Vec<_>) = v.into_iter().enumerate().partition(|(i, _)| i % 2 == 0);
    let a: Vec<_> = a.into_iter().map(|(_, v)| v).collect();
    let b: Vec<_> = b.into_iter().map(|(_, v)| v).collect();

    let a_cnt = counter(&a);
    let b_cnt = counter(&b);

    let ans = {
        let a_ma = a_cnt.iter().max_by_key(|(_, v)| *v).unwrap();
        let b_ma = b_cnt.iter().max_by_key(|(_, v)| *v).unwrap();
        n / 2 - a_ma.1 + n / 2 - b_ma.1
    };

    println!("{}", ans);
}
