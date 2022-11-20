use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        prices: (u64, u64, u64, u64),
        n: u64,
    }

    // 2L買って一番安いやつ
    let mi2 = *[prices.0 * 8, prices.1 * 4, prices.2 * 2, prices.3]
        .iter()
        .min()
        .unwrap();

    // 1L買って一番安いやつ
    let mi1 = *[prices.0 * 4, prices.1 * 2, prices.2]
        .iter()
        .min()
        .unwrap();

    let ans = (n / 2) * mi2 + (n % 2) * mi1;

    println!("{}", ans);
}
