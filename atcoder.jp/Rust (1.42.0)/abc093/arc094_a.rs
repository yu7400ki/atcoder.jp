use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        v: [i32; 3],
    }

    let max_v = v.iter().max().unwrap();
    let d = max_v * 3 - v.iter().sum::<i32>();

    println!("{}", d / 2 + d % 2 * 2);
}
