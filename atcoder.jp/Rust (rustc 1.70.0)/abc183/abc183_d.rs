use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        w: isize,
    }

    let mut vec = vec![0; 2 * 100_000 + 1];

    for _ in 0..n {
        input! {
            s: usize,
            t: usize,
            p: isize,
        }

        vec[s] += p;
        vec[t] -= p;
    }

    for i in 1..vec.len() {
        vec[i] += vec[i - 1];
    }

    let ans = vec.into_iter().all(|x| x <= w);
    if ans {
        println!("Yes");
    } else {
        println!("No");
    }
}
