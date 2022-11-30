use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut t: [(i64, i64); n],
    }

    let mut elapsed = 0;
    t.sort_by_key(|&ab| ab.1);

    for (a, b) in t {
        elapsed += a;
        if elapsed > b {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
