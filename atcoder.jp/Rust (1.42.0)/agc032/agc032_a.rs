use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut b: [usize; n],
    }

    for i in 0..n {
        if b[i] - 1 > i {
            println!("-1");
            return;
        }
    }

    let mut ans = vec![];
    while !b.is_empty() {
        for i in (0..b.len()).rev() {
            if b[i] == i + 1 {
                ans.push(b.remove(i));
                break;
            }
        }
    }

    for a in ans.iter().rev() {
        println!("{}", a);
    }
}
