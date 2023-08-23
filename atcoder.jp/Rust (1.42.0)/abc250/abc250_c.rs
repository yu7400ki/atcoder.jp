use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut idx = (0..n).collect::<Vec<usize>>();
    let mut ans = (0..n).collect::<Vec<usize>>();

    for _ in 0..q {
        input! {
            x: Usize1,
        }

        let mut i = idx[x];
        if i == n - 1 {
            i -= 1;
        }

        idx.swap(ans[i], ans[i + 1]);
        ans.swap(i, i + 1);
    }

    let ans = ans
        .iter()
        .map(|x| x + 1)
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ");

    println!("{}", ans);
}
