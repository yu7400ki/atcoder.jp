use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        s: usize,
    }

    let ans = [vec![s; k], vec![if s == 1 { 2 } else { s - 1 }; n - k]].concat();

    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
