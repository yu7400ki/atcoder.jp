use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut cnt = 1;
    let mut ans = 0;
    for i in a {
        if i == cnt {
            cnt += 1;
        } else {
            ans += 1;
        }
    }

    if ans == n {
        println!("-1");
    } else {
        println!("{}", ans);
    }
}   
