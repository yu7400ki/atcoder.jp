use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        s: [String; h],
    }

    let mut ans = s
        .iter()
        .map(|s| {
            s.chars()
                .map(|c| if c == '.' { '0' } else { '#' })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    for (y, row) in s.iter().enumerate() {
        for (x, c) in row.chars().enumerate() {
            if c != '#' {
                continue;
            }

            for i in -1..2 {
                for j in -1..2 {
                    if i == 0 && j == 0 {
                        continue;
                    }

                    let y = y as isize + i;
                    let x = x as isize + j;
                    if y < 0 || y >= h as isize || x < 0 || x >= w as isize {
                        continue;
                    }

                    let y = y as usize;
                    let x = x as usize;

                    match ans[y][x] {
                        '#' => continue,
                        '0'..='8' => ans[y][x] = (ans[y][x] as u8 + 1) as char,
                        _ => unreachable!(),
                    }
                }
            }
        }
    }

    let ans = ans
        .iter()
        .map(|row| row.iter().collect::<String>())
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", ans);
}
