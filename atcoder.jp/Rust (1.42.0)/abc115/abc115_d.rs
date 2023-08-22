use proconio::{fastout, input};

fn solve(n: isize, x: isize, patty: &[isize], layer: &[isize]) -> isize {
    if n == 0 {
        if x <= 0 {
            return 0;
        } else {
            return 1;
        }
    } else if x <= 1 + layer[(n - 1) as usize] {
        return solve(n - 1, x - 1, patty, layer);
    } else {
        return patty[(n - 1) as usize]
            + 1
            + solve(n - 1, x - 2 - layer[(n - 1) as usize], patty, layer);
    }
}

#[fastout]
fn main() {
    input! {
        n: isize,
        x: isize,
    }

    let mut patty = [1; 51];
    let mut layer = [1; 51];
    for i in 1..51 {
        patty[i] = patty[i - 1] * 2 + 1;
        layer[i] = layer[i - 1] * 2 + 3;
    }

    let ans = solve(n, x, &patty, &layer);

    println!("{}", ans);
}
