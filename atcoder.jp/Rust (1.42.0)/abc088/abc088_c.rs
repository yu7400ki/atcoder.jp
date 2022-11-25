use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        c: [(i64, i64, i64); 3],
    }

    /*
    a1 + b1, a1 + b2, a1 + b3
    a2 + b1, a2 + b2, a2 + b3
    a3 + b1, a3 + b2, a3 + b3
    */

    let (b1, b2, b3) = c[0];
    let (c21, c22, c23) = c[1];
    let (c31, c32, c33) = c[2];

    if c21 - b1 != c22 - b2 || c22 - b2 != c23 - b3 {
        println!("No");
        return;
    }

    if c31 - b1 != c32 - b2 || c32 - b2 != c33 - b3 {
        println!("No");
        return;
    }

    println!("Yes");
}
