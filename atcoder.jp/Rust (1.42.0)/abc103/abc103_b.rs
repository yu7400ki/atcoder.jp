use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
        t: String,
    }

    for i in 0..s.len() {
        if s[i..].to_string() + &s[..i] == t {
            println!("Yes");
            return;
        }
    }

    println!("No");
}   
