use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut sheet = vec![vec![0; 101]; 101];
    for _ in 0..n {
        input! {
            a: usize,
            b: usize,
            c: usize,
            d: usize,
        }
        for x in a..b {
            for y in c..d {
                sheet[x][y] = 1;
            }
        }
    }

    let ans = sheet.iter().flatten().sum::<i32>();
    println!("{}", ans);
}
