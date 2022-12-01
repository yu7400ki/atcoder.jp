use proconio::{fastout, input};
use std::collections::HashMap;

fn bfs(
    graph: &std::collections::HashMap<usize, Vec<usize>>,
    start: usize,
) -> std::collections::HashMap<usize, i32> {
    let mut queue = std::collections::VecDeque::new();
    let mut dist = std::collections::HashMap::new();
    queue.push_back(start);
    dist.insert(start, 0);
    while let Some(node) = queue.pop_front() {
        for &next in graph.get(&node).unwrap() {
            if dist.contains_key(&next) {
                continue;
            }
            dist.insert(next, dist.get(&node).unwrap() + 1);
            queue.push_back(next);
        }
    }
    dist
}

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut graph = HashMap::new();
    for _ in 0..m {
        input! {
            a: usize,
            b: usize,
        }
        graph.entry(a).or_insert(vec![]).push(b);
        graph.entry(b).or_insert(vec![]).push(a);
    }

    let dist = bfs(&graph, 1);
    let ans = dist.get(&n).unwrap_or(&-1) == &2;

    println!("{}", if ans { "POSSIBLE" } else { "IMPOSSIBLE" });
}
