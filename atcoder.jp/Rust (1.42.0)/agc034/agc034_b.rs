use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let s = s.replace("BC", "D");
    let s = s.chars().collect::<Vec<_>>();
    let splitted = s.split(|&c| ['B', 'C'].contains(&c)).collect::<Vec<_>>();

    let ans = splitted.iter().map(|&v| {
        let mut tmp = 0;
        let mut cnt = 0;
        for &c in v {
            match c {
                'A' => cnt += 1,
                'D' => tmp += cnt,
                _ => unreachable!(),
            }
        }
        tmp
    }).sum::<usize>();

    println!("{}", ans);
}
