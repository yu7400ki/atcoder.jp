use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque, HashSet};

fn bfs<T>(graph: &HashMap<T, HashSet<T>>, start: T) -> HashMap<T, usize>
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
        n1: usize,
        n2: usize,
        m: usize,
        ab: [(usize, usize); m],
    }

    let mut graph = HashMap::new();
    for (a, b) in ab {
        graph.entry(a).or_insert(HashSet::new()).insert(b);
        graph.entry(b).or_insert(HashSet::new()).insert(a);
    }

    let depth1 = bfs(&graph, 1);
    let depth2 = bfs(&graph, n1 + n2);

    let length1 = depth1.values().max().unwrap();
    let length2 = depth2.values().max().unwrap();

    println!("{}", length1 + length2 + 1);
}
