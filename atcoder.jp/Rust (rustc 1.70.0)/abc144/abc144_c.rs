use proconio::{fastout, input};

fn divisor(n: usize) -> Vec<usize> {
    let mut res = vec![];
    for i in 1..n + 1 {
        if i * i > n {
            break;
        }
        if n % i == 0 {
            res.push(i);
            if i != n / i {
                res.push(n / i);
            }
        }
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let divisors = divisor(n);
    let ans = divisors.iter().map(|&x| x + n / x - 2).min().unwrap();

    println!("{}", ans);
}
