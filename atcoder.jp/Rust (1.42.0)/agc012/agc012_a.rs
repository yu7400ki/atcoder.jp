use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i64; 3 * n],
    }

    a.sort_by(|a, b| b.cmp(a));
    
    let mut ans = 0;
    for i in (1..2 * n).step_by(2) {
        ans += a[i];
    }

    println!("{}", ans);
}
