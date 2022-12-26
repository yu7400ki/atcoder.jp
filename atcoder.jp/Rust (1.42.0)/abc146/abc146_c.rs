use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        x: i64,
    }

    let d = |n: i64| n.to_string().len() as i64;
    let f = |n: i64| a * n + b * d(n);

    let mut ok = 0;
    let mut ng = 1_000_000_000 + 1;

    while ng - ok > 1 {
        let mid = (ok + ng) / 2;
        if f(mid) <= x {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    println!("{}", ok);
}
