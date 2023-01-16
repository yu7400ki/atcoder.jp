use proconio::{fastout, input, marker::Usize1};
use std::collections::{HashMap, VecDeque};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut tree = HashMap::new();
    let mut count = vec![0; n];

    for _ in 0..n-1 {
        input! {
            a: Usize1,
            b: Usize1,
        }

        tree.entry(a).or_insert(vec![]).push(b);
        tree.entry(b).or_insert(vec![]).push(a);
    }

    for _ in 0..q {
        input! {
            p: Usize1,
            x: usize,
        }

        count[p] += x;
    }

    let mut queue = VecDeque::new();
    queue.push_back(0);
    let mut visited = vec![false; n];
    visited[0] = true;
    while let Some(node) = queue.pop_front() {
        for &child in tree[&node].iter() {
            if visited[child] {
                continue;
            }

            count[child] += count[node];
            visited[child] = true;
            queue.push_back(child);
        }
    }

    println!("{}", count.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
}
