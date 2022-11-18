use proconio::{fastout, input};

fn distance(y: &Vec<f64>, z: &Vec<f64>) -> f64 {
    let sum = y
        .iter()
        .zip(z.iter())
        .fold(0.0, |sum, (y, z)| sum + (y - z).powi(2));
    sum.sqrt()
}

#[fastout]
fn main() {
    input! {
        n: usize,
        d: usize,
        x: [[f64; d]; n],
    }

    let mut cnt = 0;
    for i in 0..n {
        for j in i + 1..n {
            if distance(&x[i], &x[j]) % 1.0 == 0.0 {
                cnt += 1;
            }
        }
    }

    println!("{}", cnt);
}
