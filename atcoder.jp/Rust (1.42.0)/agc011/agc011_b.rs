use proconio::{fastout, input};

fn accumulate<T>(v: &[T]) -> Vec<T>
where
    T: std::ops::Add<Output = T> + Copy + Default,
{
    let mut res = vec![T::default(); v.len() + 1];
    for i in 0..v.len() {
        res[i + 1] = res[i] + v[i];
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i64; n],
    }

    a.sort();
    let a_accum = accumulate(&a);

    let mut t = 0;
    for i in 1..n {
        if 2 * a_accum[i] < a[i] {
            t = i;
        }
    }

    println!("{}", n - t);
}
