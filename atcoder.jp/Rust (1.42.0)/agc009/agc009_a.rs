use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        ab: [(usize, usize); n],
    }

    let (a, b) = {
        let mut a = vec![0; n];
        let mut b = vec![0; n];
        for (i, v) in ab.into_iter().rev().enumerate() {
            a[i] = v.0;
            b[i] = v.1;
        }
        (a, b)
    };

    let mut ans = 0;

    for (v, k) in a.iter().zip(b.iter()) {
        let v = v + ans;
        let r = v % k;
        if r != 0 {
            ans += k - r;
        }
    }

    println!("{}", ans);
}
