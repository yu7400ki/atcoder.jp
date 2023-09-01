use proconio::input;


fn main() {
    input! {
        n: isize,
        y: isize,
    }

    let mut ans = (-1, -1, -1);
    'outer: for i in 0..=n {
        for j in 0..=n {
            let k = n - i - j;
            if k < 0 {
                continue 'outer;
            }
            let s = i * 10000 + j * 5000 + k * 1000;
            if s == y {
                ans = (i, j, k);
                break 'outer;
            }
        }
    }

    println!("{} {} {}", ans.0, ans.1, ans.2);
}
