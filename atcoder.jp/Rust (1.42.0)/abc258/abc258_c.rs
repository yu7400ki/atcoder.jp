use proconio::{input};

fn main() {
    let mut idx = 0;
    input! {
        n: usize,
        q: usize,
        s: String,
    };
    let s = s.chars().collect::<Vec<char>>();
    for _ in 0..q {
        input! {
            m: usize,
            x: usize,
        };
        if m == 1 {
            idx = (n - x + idx) % n;
        } else if m == 2 {
            println!("{}", s[(idx + x - 1) % n]);
        }
    };
}
