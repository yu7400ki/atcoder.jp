use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: String,
        b: String,
    }

    if a.len() == b.len() {
        if a > b {
            println!("GREATER");
        } else if a < b {
            println!("LESS");
        } else {
            println!("EQUAL");
        }
    } else {
        if a.len() > b.len() {
            println!("GREATER");
        } else {
            println!("LESS");
        }
    }
}   
