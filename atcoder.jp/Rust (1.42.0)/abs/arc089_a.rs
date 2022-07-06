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
        let dt = t - time;
        time = t;
        let dist = (x - pos[0]).abs() + (y - pos[1]).abs();
        if dist % 2 == dt % 2 && dist <= dt {
            pos[0] = x;
            pos[1] = y;
        } else {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
