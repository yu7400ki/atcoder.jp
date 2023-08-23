use proconio::{input, fastout, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut acc = vec![0; n + 1];

    for _ in 0..q {
        input! {
            l: Usize1,
            r: Usize1,
        }
        acc[l] += 1;
        acc[r + 1] -= 1;
    }

    for i in 0..n {
        acc[i + 1] += acc[i];
    }
    acc.pop();

    let ans = acc.iter().fold(true, |prev, &x| prev && x > 0);
    println!("{}", if ans { "Yes" } else { "No" });
}
