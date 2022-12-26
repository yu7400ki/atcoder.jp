use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
        b: [i64; n],
    }

    let diff = a
        .iter()
        .zip(b.iter())
        .map(|(a, b)| a - b)
        .collect::<Vec<_>>();

    let (less, greater): (Vec<i64>, Vec<i64>) = diff.iter().partition(|&&x| x < 0);

    if less.len() == 0 {
        println!("0");
        return;
    }

    let mut greater = greater
        .into_iter()
        .filter(|&x| x != 0)
        .sorted()
        .collect::<Vec<_>>();

    let mut ans = less.len();
    let mut greater_sum = 0;
    let less_sum = -less.iter().sum::<i64>();

    while greater_sum < less_sum {
        if let Some(x) = greater.pop() {
            greater_sum += x;
            ans += 1;
        } else {
            break;
        }
    }

    if greater_sum >= less_sum {
        println!("{}", ans);
    } else {
        println!("-1");
    }
}
