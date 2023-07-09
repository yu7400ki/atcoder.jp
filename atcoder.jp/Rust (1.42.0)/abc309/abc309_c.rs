use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        mut ab: [(usize, usize); n],
    }

    let mut total = ab.iter().fold(0, |p, c| p + c.1);
    ab.sort_by(|a, b| a.0.cmp(&b.0));

    if total <= k {
        println!("1");
        return;
    }

    for (a, b) in ab.into_iter() {
        total -= b;
        if total <= k {
            println!("{}", a + 1);
            return;
        }
    }
}
