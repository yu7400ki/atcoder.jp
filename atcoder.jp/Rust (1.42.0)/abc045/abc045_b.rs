use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        sa: String,
        sb: String,
        sc: String,
    }

    let mut sa = sa.chars().rev().collect::<Vec<_>>();
    let mut sb = sb.chars().rev().collect::<Vec<_>>();
    let mut sc = sc.chars().rev().collect::<Vec<_>>();

    let s = [&mut sa, &mut sb, &mut sc];
    let mut turn = 0usize;

    let winner = loop {
        if let Some(c) = s[turn].pop() {
            turn = c as usize - 'a' as usize;
        } else {
            break turn as u8 + 'A' as u8;
        }
    };

    println!("{}", winner as char);
}
