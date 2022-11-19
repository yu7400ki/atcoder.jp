use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [u64; n],
        q: usize,
    }

    let mut b: Option<u64> = None;
    let mut last_reset = 0;
    let mut add = vec![(last_reset, 0u64); n];

    for iteration in 0..q {
        input! {
            query: usize,
        }

        match query {
            1 => {
                input! {
                    x: u64,
                }
                b = Some(x);
                last_reset = iteration;
            }
            2 => {
                input! {
                    i: usize,
                    x: u64,
                }
                if add[i - 1].0 < last_reset {
                    add[i - 1] = (last_reset, x);
                } else {
                    add[i - 1].1 += x;
                }
            }
            _ => {
                input! {
                    i: usize,
                }
                let add = add[i - 1];
                println!("{}", add.1 + b.unwrap_or(a[i - 1]));
            }
        }
    }
}
