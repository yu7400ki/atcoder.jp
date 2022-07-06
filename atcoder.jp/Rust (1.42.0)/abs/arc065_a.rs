use proconio::{input, fastout};

#[fastout]
fn main() {
    let words = vec!["dream", "dreamer", "erase", "eraser"];
    let mut flag = false;
    input! {
        mut s: String,
    };

    while s.len() > 0 {
        for word in words.iter() {
            if s.ends_with(word) {
                for _ in 0..word.len() {
                    s.pop();
                }
                flag = true;
                break;
            }
        }
        if !flag {
            println!("NO");
            return;
        }
        flag = false
    }
    println!("YES");
}
