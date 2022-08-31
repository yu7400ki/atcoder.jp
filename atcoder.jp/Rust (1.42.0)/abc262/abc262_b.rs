use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut g = vec![vec![]; n+1];
    for _ in 0..m {
        input! {
            u: usize,
            v: usize,
        }
        g[u].push(v);
        g[v].push(u);
    }

    let mut ans = 0i64;

    for i in 1..=n {
        for j in i+1..=n {
            for k in j+1..=n {
                if g[i].contains(&j) && g[j].contains(&k) && g[k].contains(&i) {
                    ans += 1;
                }
            }
        }
    }

    println!("{}", ans);
}   
