use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut ans = vec![' '; 0];

    for c in s.chars() {
        match c {
            '0' => ans.push('0'),
            '1' => ans.push('1'),
            'B' => {
                ans.pop();
            }
            _ => {}
        }
    }

    println!("{}", ans.iter().collect::<String>());
}
