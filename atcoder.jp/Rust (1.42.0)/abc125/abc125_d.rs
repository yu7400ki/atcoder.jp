use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let a_abs = a.iter().map(|x| x.abs()).collect::<Vec<_>>();
    let sum = a_abs.iter().sum::<i64>();

    if a.contains(&0) {
        println!("{}", sum);
        return;
    }

    let (_plus, minus) = a.iter().partition::<Vec<&i64>, _>(|&x| x > &0);

    if minus.len() % 2 == 0 {
        println!("{}", sum);
    } else {
        let min = a_abs.iter().min().unwrap();
        println!("{}", sum - min * 2);
    }
}
