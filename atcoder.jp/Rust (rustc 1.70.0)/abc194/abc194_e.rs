use proconio::{fastout, input};
use std::collections::{BTreeSet, HashMap};

macro_rules! min {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::min($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::min($a, min!($($rest),+))
    }};
}

macro_rules! chmin {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_min = min!($($cmps),+);
        if $base > cmp_min {
            $base = cmp_min;
            true
        } else {
            false
        }
    }};
}

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; n],
    }

    let &ma = a.iter().max().unwrap();
    let mut counter: HashMap<usize, i64> = HashMap::new();
    let mut candidate: BTreeSet<usize> = (0..=ma+1).into_iter().collect();
    for i in 0..m {
        let key = a[i];
        *counter.entry(key).or_insert(0) += 1;
        candidate.remove(&key);
    }
    let &ans = candidate.first().unwrap();
    let mut ans = ans;

    for i in m..n {
        let entry = a[i];
        let leave = a[i-m];
        *counter.entry(entry).or_insert(0) += 1;
        *counter.entry(leave).or_insert(0) -= 1;
        candidate.remove(&entry);
        if *counter.get(&leave).unwrap() == 0 {
            candidate.insert(leave);
        }
        chmin!(ans, *candidate.first().unwrap());
    }

    println!("{}", ans);
}
