use proconio::{fastout, input};
use std::collections::{HashSet, VecDeque};

#[derive(Debug, Clone, Hash, Eq, PartialEq)]
struct Puzzle {
    field: Vec<Vec<usize>>,
}

impl Puzzle {
    fn new(field: Vec<Vec<usize>>) -> Self {
        Self { field }
    }

    fn swap_row(&self, i: usize) -> Self {
        let mut new_field = self.field.clone();
        new_field.swap(i, i + 1);
        Self::new(new_field)
    }

    fn swap_col(&self, i: usize) -> Self {
        let mut new_field = self.field.clone();
        for j in 0..self.field.len() {
            new_field[j].swap(i, i + 1);
        }
        Self::new(new_field)
    }
}

fn bfs(puzzle: Puzzle, goal: Puzzle) -> Result<usize, ()> {
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();

    queue.push_back((puzzle, 0));

    while let Some((puzzle, count)) = queue.pop_front() {
        if puzzle == goal {
            return Ok(count);
        }

        if visited.contains(&puzzle) {
            continue;
        }
        visited.insert(puzzle.clone());

        for i in 0..puzzle.field.len() - 1 {
            queue.push_back((puzzle.swap_row(i), count + 1));
        }

        for i in 0..puzzle.field[0].len() - 1 {
            queue.push_back((puzzle.swap_col(i), count + 1));
        }
    }

    Err(())
}

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        a: [[usize; w]; h],
        b: [[usize; w]; h],
    }

    let puzzle = Puzzle::new(a);
    let goal = Puzzle::new(b);

    match bfs(puzzle, goal) {
        Ok(count) => println!("{}", count),
        Err(_) => println!("-1"),
    }
}
