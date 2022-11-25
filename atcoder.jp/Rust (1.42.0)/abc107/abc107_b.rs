use std::vec;

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        a: [String; h],
    }
    
    let mut y_line = vec![true; h];
    let mut x_line = vec![false; w];

    let line = '.'.to_string().repeat(w);
    for (i, l) in a.iter().enumerate() {
        if l == &line {
            y_line[i] = false;
        }
    }

    for x in 0..w {
        for y in 0..h {
            if a[y].chars().nth(x).unwrap() == '#' {
                x_line[x] = true;
            }
        }
    }

    for y in 0..h {
        if !y_line[y] {
            continue;
        }

        for x in 0..w {
            if !x_line[x] {
                continue;
            }

            print!("{}", a[y].chars().nth(x).unwrap());
        }
        println!();
    }
}
