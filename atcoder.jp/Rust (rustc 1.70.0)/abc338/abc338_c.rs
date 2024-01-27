use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: [i64; n],
        a: [i64; n],
        b: [i64; n],
    }

    let max = 10i64.pow(6);
    let mut ans = 0;
    for i in 0..=max {
        let rest = q
            .iter()
            .zip(a.iter())
            .map(|(q, a)| q - a * i)
            .collect::<Vec<_>>();
        if !rest.iter().all(|&r| r >= 0) {
            break;
        }
        let j = rest
            .iter()
            .zip(b.iter())
            .map(|(r, b)| if *b == 0 { max } else { r / b })
            .min()
            .unwrap();
        ans = ans.max(i + j);
    }
    println!("{}", ans);
}
