use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut l: [u16; n],
    }
    l.sort();

    let mut ans = 0;
    for i in 0..n {
        for j in i + 1..n {
            for k in j + 1..n {
                let a = l[i];
                let b = l[j];
                let c = l[k];
                if a + b > c {
                    ans += 1;
                }
            }
        }
    }

    println!("{}", ans);
}
