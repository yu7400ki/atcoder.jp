use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s_: String,
    }

    let n = s_.chars().filter(|&c| c == 'N').count();
    let s = s_.chars().filter(|&c| c == 'S').count();
    let e = s_.chars().filter(|&c| c == 'E').count();
    let w = s_.chars().filter(|&c| c == 'W').count();

    let b1 = {
        if n != 0 && s != 0 || n == 0 && s == 0 {
            true
        } else {
            false
        }
    };
    let b2 = {
        if e != 0 && w != 0 || e == 0 && w == 0 {
            true
        } else {
            false
        }
    };

    println!("{}", if b1 && b2 { "Yes" } else { "No" });
}   
