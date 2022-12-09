use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        a: [String; h],
    }

    let a = {
        let a = [
            vec![".".repeat(w + 2)],
            a.iter().map(|s| format!(".{}.", s)).collect::<Vec<_>>(),
            vec![".".repeat(w + 2)],
        ]
        .concat();

        a.iter()
            .map(|s| {
                s.chars()
                    .map(|c| if c == '#' { 1 } else { 0 })
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>()
    };

    let mut pos = (1, 1);
    let ans = loop {
        if a[pos.0 + 1][pos.1] + a[pos.0][pos.1 + 1] != 1 {
            break "Impossible";
        }

        if a[pos.0 + 1][pos.1] == 1 {
            pos.0 += 1;
        } else {
            pos.1 += 1;
        }

        if pos == (h, w) {
            break "Possible";
        }
    };

    println!("{}", ans);
}
