use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        k: i64,
        s: i64,
    }

    let mut ans = 0;
    for x in 0..=k {
        for y in 0..=k {
            let z = s - x - y;
            if 0 <= z && z <= k {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
