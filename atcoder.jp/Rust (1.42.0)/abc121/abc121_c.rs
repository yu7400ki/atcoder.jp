use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut m: i64,
        mut ab: [(i64, i64); n],
    }

    ab.sort_by_key(|x| x.0);

    let mut ans = 0;
    for i in 0..n {
        if m <= ab[i].1 {
            ans += ab[i].0 * m;
            break;
        } else {
            ans += ab[i].0 * ab[i].1;
            m -= ab[i].1;
        }
    }

    println!("{}", ans);
}
