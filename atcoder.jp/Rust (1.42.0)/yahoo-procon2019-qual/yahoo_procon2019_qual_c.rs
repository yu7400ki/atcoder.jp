use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        k: i64,
        a: i64,
        b: i64,
    }

    if a + 1 >= b  {
        println!("{}", k + 1);
        return;
    }

    if k < a {
        println!("{}", k + 1);
        return;
    }

    let mut ans = a;
    let k = k - (a - 1);
    ans += (b - a) * (k / 2);
    if k % 2 == 1 {
        ans += 1;
    }

    println!("{}", ans);
}
