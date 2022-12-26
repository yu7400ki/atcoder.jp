use proconio::{fastout, input};
use libm::atan;

#[fastout]
fn main() {
    input! {
        a: f64,
        b: f64,
        x: f64,
    }

    let v = a.powi(2) * b;

    if x >= v / 2.0 {
        let rest = v - x;
        let tan = 2.0 * rest / a.powi(3);
        let theta = atan(tan);
        println!("{}", theta * 180.0 / std::f64::consts::PI);
    } else {
        let tan = 2.0 * x / (b.powi(2) * a);
        let theta = atan(tan);
        println!("{}", 90.0 - theta * 180.0 / std::f64::consts::PI);
    }
}
