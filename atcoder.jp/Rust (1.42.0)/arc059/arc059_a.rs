use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mi = *a.iter().min().unwrap();
    let ma = *a.iter().max().unwrap();

    let mut ans = 1 << 60;

    for i in mi..=ma {
        let sum = a.iter().fold(0, |acc, &x| acc + (x - i).pow(2));
        ans = ans.min(sum);
    }

    println!("{}", ans);
}
