use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut k: usize,
        ab: [(usize, usize); n],
    }

    let mut idx = 0;

    while k > 0 {
        let b = ab[idx].1;
        if k > b {
            k -= b;
            idx += 1;
        } else {
            break;
        }
    }

    println!("{}", ab[idx].0);
}
