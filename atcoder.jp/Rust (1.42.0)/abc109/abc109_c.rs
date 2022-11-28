use proconio::{fastout, input};

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        x: usize,
        mut a: [usize; n],
    }

    a.push(x);
    a.sort();

    let a = a.windows(2).map(|w| w[1] - w[0]).collect::<Vec<_>>();
    let ans = a.iter().fold(a[0], |acc, &x| gcd(acc, x));

    println!("{}", ans);
}   
