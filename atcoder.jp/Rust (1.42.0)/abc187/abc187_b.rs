use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        xy: [(isize, isize); n],
    }


    let mut ans = 0;
    for i in 0..n {
        for j in (i+1)..n {
            let (x1, y1) = xy[i];
            let (x2, y2) = xy[j];
            let dx = (x2 - x1).abs();
            let dy = (y2 - y1).abs();
            if dy <= dx {
                ans += 1;
            }
        }
    }

    println!("{}", ans)
}
