use proconio::{fastout, input};

fn f(x: isize) -> isize {
    if x == 0 {
        1
    } else {
        x * f(x - 1)
    }
}

#[fastout]
fn main() {
    input! {
        n: isize,
    }

    println!("{}", f(n));
}
