use proconio::{fastout, input};
use regex::Regex;

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let re = Regex::new(r"^A[a-z]{1}[a-z]*C[a-z]*[a-z]{2}$").unwrap();
    println!("{}", if re.is_match(&s) { "AC" } else { "WA" });
}   
