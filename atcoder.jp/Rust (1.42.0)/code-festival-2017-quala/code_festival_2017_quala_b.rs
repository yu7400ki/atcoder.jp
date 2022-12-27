use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: i64,
        m: i64,
        k: i64,
    }

    for i in 0..=m {
        for j in 0..=n {
            if i * (n - j) + j * (m - i) == k {
                println!("Yes");
                return;
            }
        }
    }

    println!("No");
}
