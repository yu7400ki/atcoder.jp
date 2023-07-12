use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        mut x: u64,
        k: u32,
    }

    for i in 0..k {
        x += 5 * 10_u64.pow(i);
        x -= x % 10_u64.pow(i + 1);
    }

    println!("{}", x);
}
