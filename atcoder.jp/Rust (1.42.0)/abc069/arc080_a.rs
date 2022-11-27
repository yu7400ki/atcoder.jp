use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let four = a.iter().filter(|&&x| x % 4 == 0).count();
    let two = a.iter().filter(|&&x| x % 2 == 0).count() - four;
    let one = n - four - two;

    if one <= four {
        println!("Yes");
    } else if one == four + 1 && two == 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
