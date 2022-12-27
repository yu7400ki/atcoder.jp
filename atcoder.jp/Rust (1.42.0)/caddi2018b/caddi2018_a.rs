use proconio::{fastout, input};

fn factorize(n: usize) -> Vec<usize> {
    let mut n = n;
    let mut res = Vec::new();

    while n % 2 == 0 {
        res.push(2);
        n /= 2;
    }

    let mut i = 3;
    while i * i <= n {
        if n % i == 0 {
            res.push(i);
            n /= i;
        } else {
            i += 2;
        }
    }

    if n != 1 {
        res.push(n);
    }

    res
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

#[fastout]
fn main() {
    input! {
        n: usize,
        p: usize,
    }

    let factors = factorize(p);
    let count = counter(&factors);

    let ans = count
        .iter()
        .filter(|(_, &v)| v >= n)
        .fold(1, |acc, (&k, &v)| v / n * k * acc);

    println!("{}", ans);
}
