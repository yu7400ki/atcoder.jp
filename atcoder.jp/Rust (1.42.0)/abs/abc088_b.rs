use proconio::{input, fastout};
use std::cmp::Reverse;

#[fastout]
fn main() {
    input! {
        n: i64,
        mut a: [i64; n],
    };
    a.sort_by_key(|&x| Reverse(x));

    let mut alice = 0;
    let mut bob = 0;
    for i in 0..n {
        if i % 2 == 0 {
            alice += a[i as usize];
        } else {
            bob += a[i as usize];
        }
    }
    println!("{}", alice - bob);
}