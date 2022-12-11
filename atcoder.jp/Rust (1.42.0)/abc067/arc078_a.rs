use proconio::{fastout, input};
use std::cmp::min;

fn accumulate<T>(v: &[T]) -> Vec<T>
where
    T: std::ops::Add<Output = T> + Copy + Default,
{
    let mut res = vec![T::default(); v.len() + 1];
    for i in 0..v.len() {
        res[i + 1] = res[i] + v[i];
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let a = accumulate(&a);
    let mut ans = 1 << 60;

    for i in 1..n {
        ans = min(ans, ((a[i] - a[0]) - (a[n] - a[i])).abs());
    }

    println!("{}", ans);
}
