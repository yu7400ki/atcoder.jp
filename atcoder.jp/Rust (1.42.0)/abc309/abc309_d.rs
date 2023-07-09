use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};

fn bfs<T>(graph: &HashMap<T, Vec<T>>, start: T) -> HashMap<T, usize>
where
    T: Eq + std::hash::Hash + Copy,
{
    let mut queue = VecDeque::new();
    queue.push_back(start);
    let mut depth = HashMap::new();
    depth.insert(start, 0);
    while let Some(u) = queue.pop_front() {
        for &v in graph.get(&u).unwrap_or(&Vec::new()) {
            if !depth.contains_key(&v) {
                depth.insert(v, depth[&u] + 1);
                queue.push_back(v);
            }
        }
    }
    depth
}

#[fastout]
fn main() {
    input! {
        n1: usize,
        n2: usize,
        m: usize,
    }

    let mut graph = HashMap::new();
    for _ in 0..m {
        input! {
            a: usize,
            b: usize,
        }
        graph.entry(a).or_insert(Vec::new()).push(b);
        graph.entry(b).or_insert(Vec::new()).push(a);
    }

    let depth1 = bfs(&graph, 1);
    let depth2 = bfs(&graph, n1 + n2);

    let length1 = depth1.values().max().unwrap();
    let length2 = depth2.values().max().unwrap();

    println!("{}", length1 + length2 + 1);
}
