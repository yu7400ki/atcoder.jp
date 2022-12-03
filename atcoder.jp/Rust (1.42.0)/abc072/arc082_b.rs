use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut p: [usize; n],
    }

    let mut ans = 0;
    for i in 0..n - 1 {
        if p[i] == i + 1 {
            p.swap(i, i + 1);
            ans += 1;
        }
    }

    if p[n - 1] == n {
        ans += 1;
    }

    println!("{}", ans);
}
