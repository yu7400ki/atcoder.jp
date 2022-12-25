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
    let alp = "abcdefghijklmnopqrstuvwxyz"
        .chars()
        .collect::<BTreeSet<char>>();
    let rest = alp.difference(&set).collect::<Vec<&char>>();

    if rest.is_empty() {
        for i in (0..s.len()).rev() {
            if s.chars().nth(i - 1).unwrap() > s.chars().nth(i).unwrap() {
                continue;
            }

            let set = s[i..].chars().collect::<BTreeSet<char>>();
            let mi = {
                let mut res = ' ';
                for c in set.into_iter() {
                    if c > s.chars().nth(i - 1).unwrap() {
                        res = c;
                        break;
                    }
                }
                res
            };

            let ans = s[..i - 1].to_string() + &mi.to_string();
            println!("{}", ans);
            return;
        }
    } else {
        s.push(*rest[0]);
        println!("{}", s);
    }
}
