use proconio::{fastout, input};

#[fastout]
fn main() {
    let mut idx = 0;
    input! {
        n: i32,
        q: i32,
        s: String,
    };
    for _ in 0..q {
        input! {
            m: i32,
            x: i32,
        };
        if m == 1 {
            idx = n - x + idx;
        } else if m == 2 {
            println!("{}", s.chars().nth(((idx + x - 1) % n) as usize).unwrap());
        }
    };
}
