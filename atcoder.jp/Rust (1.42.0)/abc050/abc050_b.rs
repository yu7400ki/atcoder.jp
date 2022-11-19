use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        t: [i64; n],
        m: usize,
        drink: [(usize, i64); m],
    }

    let sum = t.iter().sum::<i64>();

    for (p, x) in drink {
        println!("{}", sum - t[p - 1] + x);
    }
}   
