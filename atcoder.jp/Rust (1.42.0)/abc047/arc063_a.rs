use proconio::{fastout, input};

fn comp(s: &String) -> String {
    s.chars().fold(String::new(), |mut acc, c| {
        if acc.chars().last() != Some(c) {
            acc.push(c);
        }
        acc
    })
}

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let s = comp(&s);
    let ans = s.len() - 1;

    println!("{}", ans);
}
