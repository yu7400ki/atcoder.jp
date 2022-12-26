use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut k: usize,
        mut ab: [(usize, usize); n],
    }

    let mut idx = 0;
    ab.sort_by_key(|x| x.0);

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
