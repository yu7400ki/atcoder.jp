use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: i32,
        a: i32,
        b: i32,
    };

    let mut ans = 0;
    let mut t = 0;

    for i in 1..=n {
        let mut j = i;
        while j > 0 {
            t += j % 10;
            j /= 10;
        }
        if a <= t && t <= b {
            ans += i;
        }
        t = 0;
    }
    println!("{}", ans);
}
