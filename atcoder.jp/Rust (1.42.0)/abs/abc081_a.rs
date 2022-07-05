use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        s: String,
    };
    println!("{}", s.match_indices("1").count());
}
