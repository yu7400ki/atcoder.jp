use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        _: usize,
        s: Chars,
    }

    let great = s.iter().filter(|&&c| c == 'o').count();
    let bad = s.iter().filter(|&&c| c == 'x').count();

    let ans = if great >= 1 && bad == 0 { "Yes" } else { "No" };

    println!("{}", ans);
}
