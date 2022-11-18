use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        w: [String; n],
    }

    let set = w.iter().collect::<HashSet<_>>();

    if set.len() != n {
        println!("No");
        return;
    }

    for i in 0..n-1 {
        if w[i].chars().last().unwrap() != w[i+1].chars().next().unwrap() {
            println!("No");
            return;
        }
    }

    println!("Yes");
}   
