use proconio::{input, fastout};

fn sum(mut a: usize) -> usize {
    let mut ret = 0;
    while a > 0 {
        ret += a % 10;
        a /= 10;
    }
    ret
}

#[fastout]
fn main() {
    input! {
        a: usize,
        b: usize
    }

    let ans = sum(a).max(sum(b));
    println!("{}", ans);
}
