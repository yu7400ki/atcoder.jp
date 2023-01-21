use proconio::{fastout, input};

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }

    let g = a.iter().fold(0, |acc, x| gcd(acc, *x));
    let max = a.iter().max().unwrap();

    if k <= *max && k % g == 0 {
        println!("POSSIBLE");
    } else {
        println!("IMPOSSIBLE");
    }
}
