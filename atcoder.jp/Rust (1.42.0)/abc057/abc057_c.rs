use num_integer::Roots;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let divs = divisors(n);

    let f = |a: usize, b: usize| {
        let a_len = a.to_string().len();
        let b_len = b.to_string().len();
        return std::cmp::max(a_len, b_len);
    };

    let ans = divs.into_iter().map(|(a, b)| f(a, b)).min().unwrap();

    println!("{}", ans);
}

fn divisors(n: usize) -> Vec<(usize, usize)> {
    let mut res = Vec::new();
    let limit = (n as i64).sqrt() as usize;
    for i in 1..=limit {
        if n % i == 0 {
            res.push((i, n / i));
        }
    }
    res
}
