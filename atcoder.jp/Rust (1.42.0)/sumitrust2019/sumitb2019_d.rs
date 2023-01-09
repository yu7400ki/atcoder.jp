use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        _n: usize,
        s: String,
    }

    let mut ans = 0;
    for i in 0..10 {
        for j in 0..10 {
            for k in 0..10 {
                let idx = match s.find(&i.to_string()) {
                    Some(idx) => idx,
                    None => continue,
                };
                let idx = match s[idx + 1..].find(&j.to_string()) {
                    Some(idx_) => idx + idx_ + 1,
                    None => continue,
                };
                match s[idx + 1..].find(&k.to_string()) {
                    Some(idx_) => idx + idx_ + 1,
                    None => continue,
                };
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
