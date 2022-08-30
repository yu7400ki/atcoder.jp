use proconio::{fastout, input};
use std::cmp::{min, max};


#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut point = [0; 100001];
    let mut length = [0; 100001];

    for _ in 0..n {
        input! {
            t: usize,
            x: usize,
            a: usize,
        }
        point[t] = x;
        length[t] = a;
    }

    let mut dp = [[0; 5]; 100001];

    for i in 0..100000 {
        for j in 0..min(i+1, 5) {
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + if point[i+1] == j { length[i+1] } else { 0 });
            if j > 0 {
                dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j] + if point[i+1] == j-1 { length[i+1] } else { 0 });
            }
            if j < 4 {
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + if point[i+1] == j+1 { length[i+1] } else { 0 });
            }
        }
    }

    let ans = dp[100000].iter().max().unwrap();
    println!("{}", ans);
}   
