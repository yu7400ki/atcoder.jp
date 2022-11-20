use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let ans = a.iter().map(|x| x - 1).sum::<i64>();
    println!("{}", ans);
}   
