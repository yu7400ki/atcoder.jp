use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        s: String,
        q: usize,
    }

    let mut s = s.chars().collect::<VecDeque<_>>();
    let mut rev = false;

    for _ in 0..q {
        input! {
            t: usize,
        }

        match t {
            1 => {
                rev = !rev;
            }
            2 => {
                input! {
                    f: usize,
                    c: char,
                }

                match f {
                    1 => {
                        if !rev {
                            s.push_front(c);
                        } else {
                            s.push_back(c);
                        }
                    },
                    2 => {
                        if !rev {
                            s.push_back(c);
                        } else {
                            s.push_front(c);
                        }
                    },
                    _ => unreachable!(),
                }
            }
            _ => unreachable!(),
        }
    }

    let ans = if !rev {
        s.into_iter().collect::<String>()
    } else {
        s.into_iter().rev().collect::<String>()
    };

    println!("{}", ans);
}   
