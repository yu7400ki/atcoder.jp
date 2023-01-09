use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let both = s
        .iter()
        .filter(|s| s.starts_with("B") && s.ends_with("A"))
        .count();
    let end_a = s.iter().filter(|s| s.ends_with("A")).count() - both;
    let start_b = s.iter().filter(|s| s.starts_with("B")).count() - both;

    let ans = s.iter().map(|s| s.count("AB")).sum::<usize>()
        + if end_a == 0 && start_b == 0 {
            if both == 0 {
                0
            } else {
                both - 1
            }
        } else {
            both + std::cmp::min(end_a, start_b)
        };

    println!("{}", ans);
}

trait StringExt {
    fn count<S: AsRef<str>>(&self, s: S) -> usize;
}

impl StringExt for String {
    fn count<S: AsRef<str>>(&self, s: S) -> usize {
        let s = s.as_ref();
        let mut count = 0;
        let mut start = 0;
        while let Some(i) = self[start..].find(s) {
            count += 1;
            start += i + s.len();
        }
        count
    }
}
