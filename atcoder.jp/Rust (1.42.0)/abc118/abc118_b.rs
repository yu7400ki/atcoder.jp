use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut cnt = vec![0; m];

    for _ in 0..n {
        input! {
            k: usize,
            a: [usize; k],
        }

        for i in a {
            cnt[i - 1] += 1;
        }
    }

    let mut ans = 0;

    for c in cnt {
        if c == n {
            ans += 1;
        }
    }

    println!("{}", ans);
}   
