use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        sc: [(Usize1, usize); m],
    }

    let mut num = vec![10; n];

    for (s, c) in sc {
        if num[s] == 10 {
            num[s] = c;
        } else if num[s] != c {
            println!("-1");
            return;
        }
    }

    'outer: for i in 10i32.pow((n - 1) as u32)..10i32.pow(n as u32) {
        let i = i.to_string();
        for j in 0..n {
            if num[j] == 10 {
                continue;
            } else if num[j] != i.chars().nth(j).unwrap().to_digit(10).unwrap() as usize {
                continue 'outer;
            }
        }
        println!("{}", i);
        return;
    };

    println!("-1");
}
