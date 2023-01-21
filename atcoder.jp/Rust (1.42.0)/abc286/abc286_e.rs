use proconio::{
    fastout, input,
    marker::{Chars, Usize1},
};
use std::collections::{HashMap, HashSet};

fn bfs(
    graph: &std::collections::HashMap<usize, HashSet<usize>>,
    start: usize,
    a: &[i64],
) -> std::collections::HashMap<usize, (usize, i64)> {
    let mut queue = std::collections::VecDeque::new();
    let mut visited = std::collections::HashMap::new();
    queue.push_back(start);
    visited.insert(start, (0, a[start]));
    while let Some(node) = queue.pop_front() {
        let cost = visited[&node];
        for &next in graph.get(&node).unwrap_or(&HashSet::new()).iter() {
            if !visited.contains_key(&next) {
                visited.insert(next, (cost.0 + 1, cost.1 + a[next]));
                queue.push_back(next);
            } else if visited[&next].0 == cost.0 + 1 {
                let current = visited[&next].1;
                visited.insert(next, (cost.0 + 1, std::cmp::max(current, cost.1 + a[next])));
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
    for i in 0..n {
        input! {
            s: Chars,
        }
        for (j, c) in s.iter().enumerate() {
            if *c == 'Y' {
                graph.entry(i).or_insert(HashSet::new()).insert(j);
            }
        }
    }

    input! {
        q: usize,
    }

    for _ in 0..q {
        input! {
            u: Usize1,
            v: Usize1,
        }

        let depth = bfs(&graph, u, &a);
        if depth.contains_key(&v) {
            let (d, v) = depth[&v];
            println!("{} {}", d, v);
        } else {
            println!("Impossible");
        }
    }
}
