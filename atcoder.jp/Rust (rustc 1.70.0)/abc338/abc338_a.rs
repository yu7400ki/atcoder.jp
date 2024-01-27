use proconio::{fastout, input};
use regex::Regex;

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let ans = if is_capitalized(&s) { "Yes" } else { "No" };
    println!("{}", ans);
}

fn is_capitalized(s: &str) -> bool {
    let re = Regex::new(r"^[A-Z][a-z]*$").unwrap();
    re.is_match(s)
}
