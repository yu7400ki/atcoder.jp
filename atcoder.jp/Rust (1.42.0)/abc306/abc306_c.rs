use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [usize; n * 3],
    }

    let mut counter = vec![0; n + 1];
    let mut ans = vec![0; 0];

    for x in a {
        counter[x] += 1;
        if counter[x] == 2 {
            ans.push(x)
        }
    }

    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
