use proconio::{fastout, input};

fn ceil(a: u64, b: u64) -> u64 {
    (a + b - 1) / b
}

fn len(a: u64, b: u64, c: u64) -> u64 {
    let l = ceil(a, c);
    let r = b / c;
    r - l + 1
}

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
        a: u64,
        b: u64,
        c: u64,
        d: u64,
    }

    let e = lcm(c, d);

    println!(
        "{}",
        b - a + 1 - len(a, b, c) - len(a, b, d) + len(a, b, e)
    );
}
