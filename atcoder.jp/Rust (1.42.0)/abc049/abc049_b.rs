use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        _w: usize,
        c: [String; h],
    }

    for s in c {
        println!("{}", s);
        println!("{}", s);
    }
}   
