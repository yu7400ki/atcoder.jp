use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        _: usize,
        k: usize,
        a: [i64; k],
    }

    if k % 2 == 0 {
        let ans = a.chunks(2).fold(0, |acc, x| acc + (x[0] - x[1]).abs());
        println!("{}", ans);
    } else {
        let b = a.iter().rev().cloned().collect::<Vec<i64>>();
        let s = a
            .chunks_exact(2)
            .map(|x| (x[0] - x[1]).abs())
            .collect::<Vec<i64>>();
        let t = b
            .chunks_exact(2)
            .map(|x| (x[0] - x[1]).abs())
            .collect::<Vec<i64>>();
        let mut acc = vec![0; k / 2 + 1];
        let mut acc_rev = vec![0; k / 2 + 1];
        for i in 0..k / 2 {
            acc[i + 1] = acc[i] + s[i];
            acc_rev[i + 1] = acc_rev[i] + t[i];
        }
        acc_rev.reverse();
        let ans = acc
            .iter()
            .zip(acc_rev.iter())
            .map(|(x, y)| x + y)
            .min()
            .unwrap();
        println!("{}", ans);
    }
}
