use proconio::{fastout, input};

macro_rules! min {
    ($x:expr) => ( $x );
    ($x:expr, $($xs:expr),+) => {
        std::cmp::min($x, min!( $($xs),+ ))
    };
}

#[fastout]
fn main() {
    input! {
        abc: [i64; 3],
    }

    if abc.iter().any(|&x| x % 2 == 0) {
        println!("0");
        return;
    } else {
        println!("{}", min!(abc[0] * abc[1], abc[1] * abc[2], abc[2] * abc[0]));
    }
}
