use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut s: [i64; n],
    }

    let s = {
        s.sort();
        s
    };

    let ans = s.iter().sum::<i64>();

    if ans % 10 != 0 {
        println!("{}", ans);
        return;
    }

    let s = s.iter().filter(|&x| x % 10 != 0).collect::<Vec<_>>();
    let min = s.iter().nth(0);
    match min {
        Some(&x) => println!("{}", ans - x),
        None => println!("0"),
    }
}
