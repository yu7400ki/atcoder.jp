use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        _: usize,
        m: i32,
        s: Chars,
    }

    let mut t = 0;
    let mut u = 0;
    let mut ans = 0;

    for c in s.into_iter() {
        match c {
            '0' => {
                t = 0;
                u = 0;
            }
            '1' => t += 1,
            '2' => u += 1,
            _ => unreachable!(),
        };
        ans = ans.max(0.max(t - m) + u);
    }

    println!("{}", ans);
}
