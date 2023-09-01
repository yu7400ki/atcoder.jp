use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut fs: [(usize, usize); n]
    }

    fs.sort_by_key(|(_, s)| *s);
    fs.reverse();

    let s = fs[0].1;
    let mut ans = 0;
    for i in 1..n {
        let t = fs[i].1;
        ans = if fs[i].0 == fs[0].0 {
            ans.max(s + t / 2)
        } else {
            ans.max(s + t)
        }
    }

    println!("{}", ans);
}
