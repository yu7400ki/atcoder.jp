use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut group = [0; 9];
    let mut rest = 0;

    'outer: for rate in a {
        for i in 1..=8 {
            if rate < 400 * i {
                group[i as usize - 1] += 1;
                continue 'outer;
            }
        }
        rest += 1;
    }

    let sum = group.iter().filter(|&&x| x > 0).count();

    println!(
        "{} {}",
        if sum == 0 { 1 } else { sum },
        sum + rest
    );
}
