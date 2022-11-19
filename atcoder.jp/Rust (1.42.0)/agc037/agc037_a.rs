use proconio::{fastout, input};


#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut a: Vec<char> = Vec::new();
    let mut b: Vec<char> = Vec::new();
    let mut cnt = 0;

    for c in s.chars() {
        a.push(c);

        if a != b {
            b = a;
            a = Vec::new();
            cnt += 1;
        }
    }

    println!("{}", cnt);
}
