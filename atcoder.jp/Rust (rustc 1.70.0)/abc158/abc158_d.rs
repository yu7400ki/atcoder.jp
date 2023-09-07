use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        s: Chars,
        q: usize,
    }

    let mut ans: VecDeque<char> = s.into();
    let mut reversed = false;

    for _ in 0..q {
        input! {
            t: usize,
        }

        match t {
            1 => reversed = !reversed,
            2 => {
                input! {
                    f: usize,
                    c: char,
                }
                match (f, reversed) {
                    (1, false) | (2, true) => ans.push_front(c),
                    (1, true) | (2, false) => ans.push_back(c),
                    _ => unreachable!(),
                }
            }
            _ => unreachable!(),
        }
    }

    let ans: String = if reversed {
        ans.into_iter().rev().collect()
    } else {
        ans.into_iter().collect()
    };

    println!("{}", ans);
}
