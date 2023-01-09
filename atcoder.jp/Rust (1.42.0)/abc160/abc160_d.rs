use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: i64,
        x: i64,
        y: i64,
    }

    let mut ans = vec![0; n as usize - 1];

    for i in 1..=n {
        for j in i + 1..=n {
            let d = std::cmp::min(j - i, (x - i).abs() + 1 + (y - j).abs()) as usize;
            ans[d - 1] += 1;
        }
    }

    for i in 0..n - 1 {
        println!("{}", ans[i as usize]);
    }
}
