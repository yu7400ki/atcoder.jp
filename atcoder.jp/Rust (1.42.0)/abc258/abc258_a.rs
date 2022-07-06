use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        k: i32,
    };
    println!("{:02}:{:02}", 21+k/60, k%60);
}
