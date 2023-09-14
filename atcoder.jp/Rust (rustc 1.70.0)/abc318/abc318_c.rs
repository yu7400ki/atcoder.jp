use proconio::{input, fastout};

#[inline]
fn ceil(a: usize, b: usize) -> usize {
    (a + b - 1) / b
}

#[fastout]
fn main() {
    input! {
        n: usize,
        d: usize,
        p: usize,
        mut f: [usize; n],
    }

    f.sort();
    f.reverse();
    let mut acc = vec![0; n + 1];
    for i in 0..n {
        acc[i + 1] = acc[i] + f[i];
    }

    let mut ans = usize::MAX;
    for i in 0..=ceil(n, d) {
        let l = i * d;
        ans = ans.min((acc[n] - acc[l.min(n)]) + p * i);
    }

    println!("{}", ans);
}
