use proconio::{input, fastout};

#[fastout]
fn main() {
    let mut flag = true;
    input! {
        n: usize,
        a: [usize; n],
    };
    for num in a.iter() {
        if num % 2 == 0 {
            if !(num % 3 == 0 || num % 5 == 0) {
                flag = false
            }
        }
    };
    if flag {
        println!("APPROVED");
    } else {
        println!("DENIED")
    }
}