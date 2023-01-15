use proconio::{input};

fn main() {
    input! {
        n: usize,
        s: String,
    }

    let s = s.chars().collect::<Vec<_>>();

    for i in 1..n {
        let mut ans = 0;
        'outer: for l in 1..=n - i {
            for k in 1..=l {
                if s[k - 1] == s[k + i - 1] {
                    continue 'outer;
                }
            }
            ans = std::cmp::max(ans, l);
        }
        println!("{}", ans);
    }
}
