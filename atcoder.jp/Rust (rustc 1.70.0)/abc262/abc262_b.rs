use proconio::{input, fastout, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut graph = vec![vec![false; n]; n];

    for _ in 0..m {
        input! {
            a: Usize1,
            b: Usize1,
        }
        graph[a][b] = true;
        graph[b][a] = true;
    }

    let mut ans = 0;
    for a in 0..n {
        for b in a+1..n {
            for c in b+1..n {
                if graph[a][b] && graph[b][c] && graph[c][a] {
                    ans += 1;
                }
            }
        }
    }

    println!("{}", ans);
}
