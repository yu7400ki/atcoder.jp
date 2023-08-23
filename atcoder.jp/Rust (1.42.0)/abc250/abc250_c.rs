use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut ans = (0..n).collect::<Vec<usize>>();

    for _ in 0..q {
        input! {
            x: Usize1,
        }

        let p = ans[x];
        if p != n - 1 {
            ans.swap(p, p + 1);
        } else {
            ans.swap(p, p - 1);
        }
    }

    let ans = ans
        .iter()
        .map(|x| x + 1)
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ");

    println!("{}", ans);
}
