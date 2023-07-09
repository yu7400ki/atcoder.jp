use proconio::{input, fastout};
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
        for &v in graph.get(&u).unwrap() {
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
        n: usize,
        ab: [(usize, usize); n],
    }

    let graph = ab.into_iter().fold(HashMap::new(), |mut graph, (a, b)| {
        graph.entry(a).or_insert(vec![]).push(b);
        graph.entry(b).or_insert(vec![]).push(a);
        graph
    });

    if !graph.contains_key(&1) {
        println!("1");
        return;
    }

    let depth = bfs(&graph, 1);

    let ans = depth.keys().max().unwrap();

    println!("{}", ans);
}
