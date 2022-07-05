use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: i64,
        mut a: [i64; n],
    };

    let mut ans = 0;
    let mut flag = false;

    loop {
        for i in 0..n {
            if a[i as usize] % 2 == 0 {
                a[i as usize] /= 2;
            } else {
                flag = true;
                break;
            }
        };
        if flag {
            break;
        } else {
            ans += 1;
        }
    }

    println!("{}", ans);
}
