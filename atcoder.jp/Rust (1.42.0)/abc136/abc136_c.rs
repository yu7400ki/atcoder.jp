use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut h: [i64; n],
    }

    h.reverse();
    for i in 0..n - 1 {
        if h[i + 1] <= h[i] {
            continue;
        } else if h[i+1] - 1 <= h[i] {
            h[i + 1] -= 1;
        } else {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
