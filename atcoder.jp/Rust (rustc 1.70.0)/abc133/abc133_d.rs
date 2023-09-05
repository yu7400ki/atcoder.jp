use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let x1 = a
        .iter()
        .enumerate()
        .fold(0, |acc, (i, x)| if i % 2 == 0 { acc + x } else { acc - x });

    let mut ans = vec![0; n];
    ans[0] = x1;

    for i in 1..n {
        ans[i] = 2 * a[i - 1] - ans[i - 1];
    }

    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
