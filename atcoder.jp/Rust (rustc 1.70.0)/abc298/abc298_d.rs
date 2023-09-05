use ac_library::ModInt998244353 as MInt;
use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        q: usize,
    }

    let mut ans = MInt::new(1);
    let mut s = VecDeque::new();
    s.push_back(1);

    for _ in 0..q {
        input! {
            t: usize,
        }

        match t {
            1 => {
                input! {
                    x: i32,
                }
                s.push_back(x);
                ans = ans * 10 + x;
            }
            2 => {
                ans -= MInt::new(10).pow(s.len() as u64 - 1) * *s.front().unwrap();
                s.pop_front();
            }
            3 => {
                println!("{}", ans);
            }
            _ => unreachable!(),
        }
    }
}
