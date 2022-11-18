use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
    }

    println!("{}", "#".repeat(w + 2));
    for _ in 0..h {
        input! {
            s: String,
        }
        println!("{}", "#".to_string() + &s + "#");
    }
    println!("{}", "#".repeat(w + 2));
}   
