use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        k: usize,
        g_cap: usize,
        m_cap: usize,
    }

    let mut g = 0;
    let mut m = 0;

    for _ in 0..k {
        if g == g_cap {
            g = 0;
        } else if m == 0 {
            m = m_cap;
        } else {
            let t = m.min(g_cap - g);
            g += t;
            m -= t;
        }
    }

    println!("{} {}", g, m);
}
