use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let a_sorted = {
        let mut a = a.clone();
        a.sort();
        a.reverse();
        a
    };

    for i in a.iter() {
        if *i == a_sorted[0] {
            println!("{}", a_sorted[1]);
        }  else {
            println!("{}", a_sorted[0]);
        }
    }
}   
