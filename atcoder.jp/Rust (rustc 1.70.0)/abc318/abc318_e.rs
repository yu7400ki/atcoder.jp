use proconio::{input, fastout, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [Usize1; n],
    }

    let mut ans = 0_u64;
    let mut lef = vec![0; n];
    let mut rig = vec![0; n];
    for i in 0..n {
        rig[a[i]] += 1;
    }

    let mut comb = 0_u64;
    for j in 1..n - 1 {
        let diff = a[j - 1];
        lef[diff] += 1;
        rig[diff] -= 1;
        comb += lef[diff] * rig[diff];
        comb -= lef[a[j]] * rig[a[j]];
        ans += comb;
    }

    println!("{}", ans);
}
