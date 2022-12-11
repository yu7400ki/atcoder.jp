use proconio::{fastout, input};

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: u64, b: u64) -> u64 {
    a / gcd(a, b) * b
}

#[fastout]
fn main() {
    input! {
        n: usize,
        t: [u64; n],
    }

    let ans = t.iter().fold(1, |acc, &x| lcm(acc, x));

    println!("{}", ans);
}
