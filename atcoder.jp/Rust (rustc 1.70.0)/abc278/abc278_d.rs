use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
        q: usize,
    }

    let mut v = 0;

    for _ in 0..q {
        input! {
            t: usize,
        }
        match t {
            1 => {
                input! {
                    x: usize,
                }
                v = x;
                a = vec![0; n];
            }
            2 => {
                input! {
                    i: usize,
                    x: usize,
                }
                a[i - 1] += x;
            }
            3 => {
                input! {
                    i: usize,
                }
                println!("{}", a[i - 1] + v);
            }
            _ => unreachable!(),
        }
    }
}
