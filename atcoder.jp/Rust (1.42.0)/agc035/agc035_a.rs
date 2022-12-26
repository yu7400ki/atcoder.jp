use proconio::{fastout, input};

fn counter<T>(v: &[T]) -> std::collections::HashMap<T, usize>
where
    T: std::cmp::Eq + std::hash::Hash + Copy,
{
    v.iter()
        .fold(std::collections::HashMap::new(), |mut acc, &x| {
            *acc.entry(x).or_insert(0) += 1;
            acc
        })
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [u64; n],
    }

    let count = counter(&a);

    if count.get(&0).unwrap_or(&0) == &n {
        println!("Yes");
        return;
    } else if count.len() == 2 {
        let zeros = *count.get(&0).unwrap_or(&0);
        if n % 3 == 0 && zeros == n / 3 {
            println!("Yes");
            return;
        }
    } else if count.len() == 3 {
        let mut iter = count.iter();
        let (a, a_cnt) = iter.next().unwrap();
        let (b, b_cnt) = iter.next().unwrap();
        let (c, c_cnt) = iter.next().unwrap();

        if n % 3 == 0 && *a_cnt == n / 3 && *b_cnt == n / 3 && *c_cnt == n / 3 && a ^ b ^ c == 0 {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
