use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut map = vec![vec![0usize; 0]; n];

    for _ in 0..m {
        input! {
            a: usize,
            b: usize,
        }

        map[a - 1].push(b);
        map[b - 1].push(a);
    }

    for i in 0..n {
        if map[i].len() == 0 {
            println!("0");
        } else {
            print!("{} ", map[i].len());
            map[i].sort();
            for j in 0..map[i].len()-1 {
                print!("{} ", map[i][j]);
            }
            println!("{}", map[i][map[i].len()-1]);
        }
    }
}
