use proconio::{fastout, input};
use regex::Regex;

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let re = Regex::new(r"^A[a-z]+C[a-z]+$").unwrap();
    println!("{}", if re.is_match(&s) { "AC" } else { "WA" });
}   
