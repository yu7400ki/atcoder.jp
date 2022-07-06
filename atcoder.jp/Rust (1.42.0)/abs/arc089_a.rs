use proconio::{input, fastout};

#[fastout]
fn main() {
    let mut pos = [0; 2];
    let mut time = 0;
    input! {
        n: i32,
    };

    for _ in 0..n {
        input! {
            t: i32,
            x: i32,
            y: i32,
        };
        time = t - time;
        let dist = (x - pos[0]).abs() + (y - pos[1]).abs();
        if dist <= time && dist % 2 == time % 2 {
            pos[0] = x;
            pos[1] = y;
        } else {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
