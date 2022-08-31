use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        y: i32,
    }

    for i in y..y+4 {
        if i % 4 == 2 {
            println!("{}", i);
            return;
        }
    }
}   
