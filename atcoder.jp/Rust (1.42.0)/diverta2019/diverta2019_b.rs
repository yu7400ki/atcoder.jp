use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        r: i64,
        g: i64,
        b: i64,
        n: i64,
    }

    let mut ans = 0;

    for i in 0..3001 {
        for j in 0..3001 {
            let k = n - r * i - g * j;
            if k >= 0 && k % b == 0 {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
