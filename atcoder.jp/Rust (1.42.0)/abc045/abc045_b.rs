use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: [String; 3],
    }

    let mut s = s
        .into_iter()
        .map(|s| s.chars().rev().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut turn = 0;

    let winner = loop {
        if let Some(c) = s[turn].pop() {
            turn = c as usize - 'a' as usize;
        } else {
            break turn as u8 + 'A' as u8;
        }
    };

    println!("{}", winner as char);
}
