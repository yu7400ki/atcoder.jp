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

    let ok = {
        let num = num.clone();
        move |x: usize| -> bool {
            let x = x.to_string();
            if x.len() != num.len() {
                return false;
            }

            for (i, c) in x.chars().enumerate() {
                if num[i] != 10 && num[i] != c.to_digit(10).unwrap() as usize {
                    return false;
                }
            }

            true
        }
    };

    for i in 0..1000 {
        if ok(i) {
            println!("{}", i);
            return;
        }
    }

    println!("-1");
}
