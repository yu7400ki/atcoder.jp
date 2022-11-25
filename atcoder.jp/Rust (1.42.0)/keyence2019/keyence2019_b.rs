use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    if s == "keyence".to_string() {
        println!("YES");
        return;
    }
    
    let len = s.len();

    for left in 0..len {
        for right in left+1..len {
            let mut s = s.clone();
            s.replace_range(left..right, "");
            if s == "keyence".to_string() {
                println!("YES");
                return;
            }
        }
    }

    println!("NO");
}
