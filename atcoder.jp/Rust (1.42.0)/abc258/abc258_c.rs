use proconio::{fastout, input};

#[fastout]
fn main() {
    let mut idx = 0;
    input! {
        n: usize,
        q: usize,
        s: String,
        queries: [(usize, usize); q],
    };
    let s = s.chars().collect::<Vec<char>>();
    let mut ans: Vec<char> = vec![];
    for (m, x) in &queries {
        match m {
            1 => {
                idx = (idx + n - x) % n
            }
            2 => {
                ans.push(s[(idx + x - 1) % n]);
            }
            _ => {
                unreachable!();
            }
        }
    }
    for a in ans {
        println!("{}", a);
    }
}
