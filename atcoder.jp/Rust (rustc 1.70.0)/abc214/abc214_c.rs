use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        s: [usize; n],
        t: [usize; n],
    }

    let (i, t_min) = t.iter().enumerate().min_by_key(|&(_, t)| t).unwrap();
    let mut ans = vec![usize::MAX; n];
    ans[i] = *t_min;

    for j in i+1..n+i {
        let j = j % n;
        let k = if j == 0 { n-1 } else { j-1 };
        ans[j] = ans[k] + s[k];
        ans[j] = ans[j].min(t[j]);
    }

    for a in ans {
        println!("{}", a);
    }
}
