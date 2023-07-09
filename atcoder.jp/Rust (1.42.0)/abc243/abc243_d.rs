use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        _n: usize,
        x: usize,
        s: Chars,
    }

    let s = s.into_iter().fold(Vec::new(), |mut p, c| {
        match c {
            'U' => {
                if vec![Some(&'R'), Some(&'L')].contains(&p.last()) {
                    p.pop();
                } else {
                    p.push(c);
                }
            }
            _ => p.push(c),
        }
        p
    });

    let mut ans = x;
    for c in s {
        ans = match c {
            'U' => ans >> 1,
            'L' => ans << 1,
            'R' => (ans << 1) + 1,
            _ => unreachable!(),
        };
    }
    println!("{}", ans);
}
