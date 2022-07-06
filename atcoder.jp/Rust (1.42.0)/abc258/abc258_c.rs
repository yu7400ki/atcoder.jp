use proconio::{fastout, input};

#[fastout]
fn main() {
    let mut idx = 0;
    input! {
        n: usize,
        q: usize,
        s: String,
    };
    for _ in 0..q {
        input! {
            m: usize,
            x: usize,
        };
        if m == 1 {
            idx = n - x + idx;
        } else if m == 2 {
            println!("{}", s.chars().nth((idx + x - 1) % n).unwrap());
        }
    };
}
