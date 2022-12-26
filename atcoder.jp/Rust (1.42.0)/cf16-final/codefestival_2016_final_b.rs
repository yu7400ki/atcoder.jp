use proconio::{fastout, input};

fn s(n: usize) -> usize {
    (n + 1) * n / 2
}

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut ok = 0;
    let mut ng = n + 1;
    
    while ng - ok > 1 {
        let mid = (ok + ng) / 2;
        if s(mid) < n {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    let ok = ok + 1;

    let other = s(ok) - n;
    for i in 1..=ok {
        if i == other {
            continue;
        }
        println!("{}", i);
    }
}
