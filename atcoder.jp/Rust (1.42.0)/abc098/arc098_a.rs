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
        s: String,
    }

    let e_accum = accumulate(
        &s.chars()
            .map(|c| match c {
                'E' => 1,
                _ => 0,
            })
            .collect::<Vec<_>>(),
    );

    let w_accum = accumulate(
        &s.chars()
            .map(|c| match c {
                'W' => 1,
                _ => 0,
            })
            .collect::<Vec<_>>(),
    );

    let mut ans = 1i64 << 60;
    for i in 0..n {
        let w = w_accum[i];
        let e = e_accum[n] - e_accum[i + 1];
        ans = ans.min(e + w);
    }

    println!("{}", ans);
}
