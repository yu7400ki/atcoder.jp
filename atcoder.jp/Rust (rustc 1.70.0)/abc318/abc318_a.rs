use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        p: usize,
    }

    let ans = (m..=n).step_by(p).count();
    println!("{}", ans);
}
