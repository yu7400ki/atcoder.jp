use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut count = vec![0; n];

    for _ in 0..m {
        input! {
            a: usize,
            b: usize,
        }

        count[a - 1] += 1;
        count[b - 1] += 1;
    }

    count.iter().for_each(|c| println!("{}", c));
}
