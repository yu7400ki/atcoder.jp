use proconio::{input, fastout};
use std::collections::HashSet;

fn f(n: usize) -> usize {
    if n % 2 == 0 {
        n / 2
    } else {
        3 * n + 1
    }
}

#[fastout]
fn main() {
    input! {
        mut s: usize,
    }

    let mut set = HashSet::new();
    set.insert(s);

    for i in 2.. {
        s = f(s);
        if set.contains(&s) {
            println!("{}", i);
            return;
        }
        set.insert(s);
    }
}
