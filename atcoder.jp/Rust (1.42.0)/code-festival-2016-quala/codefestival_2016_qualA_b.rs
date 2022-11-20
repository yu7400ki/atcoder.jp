use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [Usize1; n],
    }

    let mut ans = 0;

    for i in 0..n {
        let idx = a[i];
        if a[idx] == i {
            ans += 1;
        }
    }

    println!("{}", ans / 2);
}
