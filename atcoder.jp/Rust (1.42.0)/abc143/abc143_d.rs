use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        l: [i64; n],
    }

    let mut ans = 0;
    for i in 0..l.len() {
        for j in i + 1..l.len() {
            for k in j + 1..l.len() {
                let a = l[i];
                let b = l[j];
                let c = l[k];
                if a < b + c && b < c + a && c < a + b {
                    ans += 1;
                }
            }
        }
    }

    println!("{}", ans);
}
