use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        x: usize,
    }

    let mut a = vec![false; x + 1];
    a[0] = true;
    let prices = [100, 101, 102, 103, 104, 105];

    for p in prices.iter() {
        for i in 0..x {
            if !a[i] {
                continue;
            }

            for j in 1..(x - i) / p + 1 {
                a[i + p * j] = true;
            }
        }
    }

    println!("{}", if a[x] { 1 } else { 0 });
}
