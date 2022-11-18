use proconio::{fastout, input};

fn distance(y: &Vec<f64>, x: &Vec<f64>) -> f64 {
    let mut sum = 0.0;
    for i in 0..y.len() {
        sum += (y[i] - x[i]).powi(2);
    }
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
