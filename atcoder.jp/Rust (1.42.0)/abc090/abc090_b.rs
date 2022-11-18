use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i32,
        b: i32,
    }

    let mut cnt = 0;

    for i in a..=b {
        let s = i.to_string();
        if s == s.chars().rev().collect::<String>() {
            cnt += 1;
        }
    }

    println!("{}", cnt);
}   
