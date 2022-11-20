use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: u32,
        k: u64,
    }

    let ans = k * (k - 1).pow(n - 1);
    println!("{}", ans);
}
