use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        a: i32,
        b: i32,
        c: i32,
        x: i32,
    };

    let mut ans = 0;
    let mut t = 0;

    for i in 0..=a {
        for j in 0..=b {
            t = (x - (i*500 + j*100)) / 50;
            if t <= c && t >= 0 {
                ans += 1;
            }
        }
    };

    println!("{}", ans);
}
