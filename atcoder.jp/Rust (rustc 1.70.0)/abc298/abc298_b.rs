use proconio::{fastout, input};

fn check(a: &Vec<Vec<usize>>, b: &Vec<Vec<usize>>) -> bool {
    for (row_a, row_b) in a.iter().zip(b.iter()) {
        for (&a, &b) in row_a.iter().zip(row_b.iter()) {
            if a == 1 && b == 0 {
                return false;
            }
        }
    }
    true
}

fn rotate(a: &Vec<Vec<usize>>) -> Vec<Vec<usize>> {
    let n = a.len();
    let mut b = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            b[j][n - i - 1] = a[i][j];
        }
    }
    b
}

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [[usize; n]; n],
        b: [[usize; n]; n],
    }

    let mut ans = "No";
    for _ in 0..4 {
        if check(&a, &b) {
            ans = "Yes";
            break;
        }
        a = rotate(&a);
    }

    println!("{}", ans);
}
