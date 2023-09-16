use pathfinding::prelude::directions::S;
use proconio::{input, fastout, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut points = vec![vec![None; n]; n];
    let mut edges = vec![vec![0; 0]; n];

    for _ in 0..m {
        input! {
            a: Usize1,
            b: Usize1,
            x: i64,
            y: i64
        }
        points[a][b] = Some((x, y));
        points[b][a] = Some((-x, -y));
        edges[a].push(b);
        edges[b].push(a);
    }

    let mut dist = vec![-1; n];
    let mut nodes = vec![vec![0; 0]; n];
    dist[0] = 0;
    nodes[0] = vec![0];
    let mut ans = vec![None; n];
    ans[0] = Some((0, 0));

    for k in 1..n {
        let mut new_nodes = vec![0; 0];
        for v in nodes[k - 1].iter() {
            for u in edges[*v].iter() {
                if dist[*u] == -1 {
                    dist[*u] = dist[*v] + 1;
                    new_nodes.push(*u);
                    let (dx, dy) = points[*v][*u].unwrap_or((0, 0));
                    let (x, y) = ans[*v].unwrap_or((0, 0));
                    ans[*u] = Some((x + dx, y + dy));
                }
            }
        }
        nodes[k] = new_nodes;
    }

    for i in 0..n {
        if ans[i].is_none() {
            println!("undecidable");
        } else {
            println!("{} {}", ans[i].unwrap().0, ans[i].unwrap().1);
        }
    }
}
