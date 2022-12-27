use proconio::{fastout, input};

fn counter<T>(v: &[T]) -> std::collections::BTreeMap<T, usize>
where
    T: std::cmp::Eq + std::hash::Hash + Copy + Ord,
{
    v.iter()
        .fold(std::collections::BTreeMap::new(), |mut map, &x| {
            *map.entry(x).or_insert(0) += 1;
            map
        })
}

#[fastout]
fn main() {
    input! {
        n: usize,
        v: [usize; n],
    }

    let cnt = counter(&v);
    if cnt.len() == 1 {
        println!("{}", n / 2);
        return;
    }

    let (a, b): (Vec<_>, Vec<_>) = v.into_iter().enumerate().partition(|(i, _)| i % 2 == 0);
    let a: Vec<_> = a.into_iter().map(|(_, v)| v).collect();
    let b: Vec<_> = b.into_iter().map(|(_, v)| v).collect();

    let mut a_cnt = counter(&a).into_iter().collect::<Vec<_>>();
    let mut b_cnt = counter(&b).into_iter().collect::<Vec<_>>();

    let ans = {
        let a_ma = a_cnt.pop().unwrap();
        let b_ma = b_cnt.pop().unwrap();

        if a_ma.0 == b_ma.0 {
            let next_a = a_cnt.pop();
            let next_b = b_cnt.pop();

            match (next_a, next_b) {
                (Some(next_a), Some(next_b)) => {
                    let a = n / 2 - a_ma.1 + n / 2 - next_b.1;
                    let b = n / 2 - b_ma.1 + n / 2 - next_a.1;
                    std::cmp::min(a, b)
                }
                (Some(next_a), None) => {
                    n / 2 - b_ma.1 + n / 2 - next_a.1
                }
                (None, Some(next_b)) => {
                    n / 2 - a_ma.1 + n / 2 - next_b.1
                }
                _ => unreachable!(),
            }
        } else {
            n / 2 - a_ma.1 + n / 2 - b_ma.1
        }
    };

    println!("{}", ans);
}
