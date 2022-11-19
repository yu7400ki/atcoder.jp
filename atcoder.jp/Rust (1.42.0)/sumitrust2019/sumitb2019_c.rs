use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        x: usize,
    }

    let mut a = vec![false; x + 1];
    a[0] = true;
    let prices = [100, 101, 102, 103, 104, 105];

    for i in 0..x+1 {
        if !a[i] {
            continue;
        }

        for &p in prices.iter() {
            if i + p <= x {
                a[i + p] = true;
            }
        }
    }

    println!("{}", if a[x] { 1 } else { 0 });
}
