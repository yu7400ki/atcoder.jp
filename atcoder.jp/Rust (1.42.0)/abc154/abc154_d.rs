use proconio::{fastout, input};

fn sun(n: f64) -> f64 {
    (1.0 + n) * n / 2.0
}

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        p: [f64; n],
    }

    let p = p.iter().map(|&x| sun(x) / x).collect::<Vec<f64>>();
    let p_acc = vec![0.0]
        .into_iter()
        .chain(p.iter().scan(0.0, |acc, &x| {
            *acc += x;
            Some(*acc)
        }))
        .collect::<Vec<f64>>();

    let mut ans: f64 = 0.0;
    for i in 0..n-k+1 {
        ans = ans.max(p_acc[i+k] - p_acc[i]);
    }

    println!("{}", ans);
}
