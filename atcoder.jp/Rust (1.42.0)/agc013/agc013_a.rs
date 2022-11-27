use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut increase = true;
    let mut decrease = true;
    let mut ans = 1i64;

    for i in 1..n {
        let rev = a[i - 1];
        if a[i] < rev {
            increase = false;
        } else if a[i] > rev {
            decrease = false;
        }

        if !(increase || decrease) {
            ans += 1;
            increase = true;
            decrease = true;
        }
    }

    println!("{}", ans);
}
