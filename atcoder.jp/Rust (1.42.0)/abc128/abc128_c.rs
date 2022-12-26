use proconio::input;
use proconio::marker::Usize1;

fn main() {
    input! {
        n: u32,
        m: usize,
    }

    let mut s = vec![0; m];
    for i in 0..m {
        input! {
            k: usize,
            a: [Usize1; k],
        }
        for j in a {
            s[i] |= 1 << j;
        }
    }

    input! {
        p: [u32; m],
    }

    let mut ans = 0;

    'outer: for i in 0..2usize.pow(n) {
        for j in 0..m {
            let mask = s[j];
            let on = i & mask;
            if on.count_ones() % 2 != p[j] {
                continue 'outer;
            }
        }
        ans += 1;
    }

    println!("{}", ans);
}
