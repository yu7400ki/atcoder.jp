use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    println!("{}", s.chars().nth(s.len()/2).unwrap());
}   
