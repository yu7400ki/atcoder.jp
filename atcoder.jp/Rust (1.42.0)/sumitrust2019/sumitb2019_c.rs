use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        x: i64,
    }

    let price = vec![100, 101, 102, 103, 104, 105];

    for i in 1..2usize.pow(6) {
        let mut sum = 0;
        for j in 0..6usize {
            if i >> j & 1 == 1 {
                sum += price[j];
            }
        }
        if x % sum == 0 {
            println!("1");
            return;
        }
    }

    println!("0");
}
