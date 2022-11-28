use proconio::{fastout, input};

fn vec_split_zeros(v: &Vec<i64>) -> Vec<Vec<i64>> {
    let mut res = Vec::new();
    let mut tmp = Vec::new();
    for i in 0..v.len() {
        if v[i] == 0 {
            if tmp.len() > 0 {
                res.push(tmp);
                tmp = Vec::new();
            }
        } else {
            tmp.push(v[i]);
        }
    }
    if tmp.len() > 0 {
        res.push(tmp);
    }
    res
}

fn solve(v: &Vec<i64>) -> i64 {
    if v.len() <= 1 {
        return v[0]
    }

    let mi = v.iter().min().unwrap();
    mi + vec_split_zeros(&v.iter().map(|x| x - mi).collect::<Vec<i64>>()).iter().map(|x| solve(x)).sum::<i64>()
}
#[fastout]
fn main() {
    input! {
        n: usize,
        h: [i64; n],
    }

    println!("{}", solve(&h));
}
