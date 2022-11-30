use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let a = [vec![0i64; 1], a, vec![0i64; 1]].concat();

    let d = a.windows(2).map(|w| (w[1] - w[0]).abs()).sum::<i64>();

    for i in 1..=n {
        let mut ans = d;
        ans -= (a[i] - a[i - 1]).abs();
        ans -= (a[i + 1] - a[i]).abs();
        ans += (a[i + 1] - a[i - 1]).abs();
        println!("{}", ans);
    }
}
