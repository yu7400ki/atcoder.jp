use proconio::{fastout, input};
use std::collections::HashMap;

fn bfs(graph: &std::collections::HashMap<i64, Vec<i64>>, start: i64) -> std::collections::HashMap<i64, i64> {
    let mut queue = std::collections::VecDeque::new();
    let mut visited = std::collections::HashMap::new();
    queue.push_back(start);
    visited.insert(start, 0);
    while let Some(node) = queue.pop_front() {
        let cost = visited[&node];
        for &next in graph.get(&node).unwrap().iter() {
            if !visited.contains_key(&next) {
                visited.insert(next, cost + 1);
                queue.push_back(next);
            }
        }
    }
    visited
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut graph = HashMap::new();
    for i in 0..n as i64 {
        graph.entry(i).or_insert(vec![]).push(a[i as usize] - 1);
    }

    println!("{}", bfs(&graph, 0).get(&1).unwrap_or(&-1));
}
