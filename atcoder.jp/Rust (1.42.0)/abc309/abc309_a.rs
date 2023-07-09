use num_integer::div_mod_floor;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: isize,
        b: isize,
    }

    let (ya, xa) = div_mod_floor(a - 1, 3);
    let (yb, xb) = div_mod_floor(b - 1, 3);

    if (xa - xb).abs() == 1 && ya == yb {
        println!("Yes")
    } else {
        println!("No")
    }
}
