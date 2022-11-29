use proconio::{fastout, input};


#[fastout]
fn main() {
    input! {
        x: i64,
    }

    let a = 1;
    let b = 1;
    let c = -2 * x;

    let d = b * b - 4 * a * c;

    let ans = (-b as f64 + (d as f64).sqrt()) / (2 * a) as f64;

    println!("{}", ans.ceil());
}
