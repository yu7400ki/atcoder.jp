use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut ab: [(isize, isize); n],
    }

    let mut gap = ab.iter().fold(0, |p, (c, _)| p + c);
    ab.sort_by_key(|(a, b)| -(a * 2 + b));

    let mut ans = 0;
    while gap >= 0 {
        let (a, b) = ab[ans];
        gap -= a * 2 + b;
        ans += 1;
    }

    println!("{}", ans);
}
