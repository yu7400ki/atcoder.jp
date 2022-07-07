use proconio::{fastout, input};

fn prime(n: usize) -> Vec<usize> {
    let mut prime = vec![true; n + 1];
    prime[0] = false;
    prime[1] = false;
    for i in 2..(n + 1) {
        if prime[i] {
            for j in (i * i..(n + 1)).step_by(i) {
                prime[j] = false;
            }
        }
    }
    prime
        .iter()
        .enumerate()
        .filter(|&(_, &p)| p)
        .map(|(i, _)| i)
        .collect()
}

const LIMIT: usize = 1000000;

#[fastout]
fn main() {
    let primes = prime(LIMIT);
    let mut ans = 0;
    input! {
        n: usize,
    };

    for i in 1..primes.len() {
        let a = primes[i].pow(3);
        if a * 2 > n {
            break;
        }
        let mut ok: usize = 0;
        let mut ng: usize = i;
        while (ng - ok) > 1 {
            let mid = (ok + ng) / 2;
            if a * primes[mid] <= n {
                ok = mid;
            } else {
                ng = mid;
            }
        };
        ans += ok + 1;
    }
    println!("{}", ans);
}
