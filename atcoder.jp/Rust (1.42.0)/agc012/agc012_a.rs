use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i64; 3 * n],
    }

    a.sort();
    let ans = a
        .iter()
        .chunks(n)
        .into_iter()
        .enumerate()
        .fold(vec![vec![0i64; 3]; n], |mut acc, (i, c)| {
            c.enumerate().for_each(|(j, &v)| {
                acc[j][i] = v;
            });
            acc
        })
        .iter()
        .fold(0, |acc, v| acc + v[1]);

    println!("{}", ans);
}
