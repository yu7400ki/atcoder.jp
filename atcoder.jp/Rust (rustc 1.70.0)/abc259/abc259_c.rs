use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        s: String,
        t: String,
    }

    let s = rle(&s);
    let t = rle(&t);

    if s.len() != t.len() {
        println!("No");
        return;
    }

    for ((sc, sn), (ts, tn)) in s.into_iter().zip(t.into_iter()) {
        if sc != ts {
            println!("No");
            return;
        }
        if sn > tn {
            println!("No");
            return;
        }
        if sn == 1 && tn > 1 {
            println!("No");
            return;
        }
    }

    println!("Yes");
}

fn rle(s: &String) -> Vec<(char, usize)> {
    let mut ret = Vec::new();
    let mut prev = s.chars().next().unwrap();
    let mut count = 1;
    for c in s.chars().skip(1) {
        if c == prev {
            count += 1;
        } else {
            ret.push((prev, count));
            prev = c;
            count = 1;
        }
    }
    ret.push((prev, count));
    ret
}
