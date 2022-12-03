use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: usize,
        b: usize,
        c: usize,
        d: usize,
        s: String,
    }
    let s = s.chars().collect::<Vec<_>>();

    if c < d {
        let v = s[a - 1..c].iter().collect::<String>();
        let w = s[b - 1..d].iter().collect::<String>();
        if v.contains("##") || w.contains("##") {
            println!("No");
            return;
        }
    } else {
        let v = s[b - 1..d].iter().collect::<String>();
        if v.contains("...") {
            let v = s[a - 1..c].iter().collect::<String>();
            let w = s[b - 1..d].iter().collect::<String>();
            if v.contains("##") || w.contains("##") {
                println!("No");
                return;
            }
        } else {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
