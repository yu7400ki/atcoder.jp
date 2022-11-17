use proconio::{fastout, input};

fn gcd(a: &u64, b: &u64) -> u64 {
    if b == &0 {
        *a
    } else {
        gcd(b, &(a % b))
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [u64; n],
    }

    let start = a[0];
    let ans = a.into_iter().fold(start, |a, b| gcd(&a, &b));
    println!("{}", ans);
}   
