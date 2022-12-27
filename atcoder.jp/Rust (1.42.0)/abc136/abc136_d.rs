use proconio::marker::Chars;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: Chars,
    }

    let n = s.len();
    let mut ans = vec![0; n];

    {
        let mut cnt = 0;
        for i in 0..n {
            match s[i] {
                'R' => cnt += 1,
                'L' => {
                    ans[i] += cnt / 2;
                    ans[i - 1] += cnt - cnt / 2;
                    cnt = 0;
                }
                _ => unreachable!(),
            }
        }
    }

    {
        let mut cnt = 0;
        for i in (0..n).rev() {
            match s[i] {
                'L' => cnt += 1,
                'R' => {
                    ans[i] += cnt / 2;
                    ans[i + 1] += cnt - cnt / 2;
                    cnt = 0;
                }
                _ => unreachable!(),
            }
        }
    }

    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
