use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        h: [i64; n],
    }

    let mut ans = 0;
    let mut cnt = 0;
    let mut pos = 0;

    for next in 1..n {
        if h[next] <= h[pos] {
            cnt += 1;
        } else {
            ans = std::cmp::max(ans, cnt);
            cnt = 0;
        }
        pos = next;
    }

    ans = std::cmp::max(ans, cnt);
    println!("{}", ans);
}   
