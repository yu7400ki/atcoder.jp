use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {
        mut s: String,
    }

    if s == "zyxwvutsrqponmlkjihgfedcba" {
        println!("-1");
        return;
    }

    let set = s.chars().collect::<BTreeSet<char>>();
    let alp = "abcdefghijklmnopqrstuvwxyz".chars().collect::<BTreeSet<char>>();
    let rest = alp.difference(&set).collect::<Vec<&char>>();

    if rest.is_empty() {
        for i in (0..s.len()).rev() {
            let set = s[0..i].chars().collect::<BTreeSet<char>>();
            let c = s.chars().nth(i).unwrap();
            if c == 'z' {
                continue;
            }
            let next = (c as u8 + 1) as char;
            if set.contains(&next) {
                continue;
            }
            let ans = s[0..i].to_string() + &next.to_string();
            println!("{}", ans);
            return;
        }

    } else {
        s.push(*rest[0]);
        println!("{}", s);
    }
}
