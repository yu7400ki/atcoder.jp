use proconio::{input, fastout, marker::Chars};

#[fastout]
fn main() {
    input! {
        s: Chars,
    }

    let mut ans = 0;
    let mut res = Vec::new();

    for c in s {
        if let Some(&last) = res.last() {
            if last != c {
                res.pop();
                ans += 2;
            } else {
                res.push(c);
            }
        } else {
            res.push(c);
        }
    }

    println!("{}", ans);
}
