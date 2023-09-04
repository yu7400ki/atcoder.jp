use proconio::{fastout, input};
use std::{
    collections::{BTreeSet, HashMap},
    hash::Hash,
};

fn repeat(s: &String, n: usize, sep: &str) -> String {
    let mut ret = String::new();
    if n == 0 {
        return ret;
    }
    ret += s;
    for _ in 1..n {
        ret += sep;
        ret += s;
    }
    ret
}

#[fastout]
fn main() {
    input! {
        _n: usize,
        q: usize,
    }

    let mut boxes = vec![MultiSet::new(); 2 * 10_i32.pow(5) as usize + 1];
    let mut cards = vec![MultiSet::new(); 2 * 10_i32.pow(5) as usize + 1];

    for _ in 0..q {
        input! {
            t: usize,
        }

        match t {
            1 => {
                input! {
                    i: usize,
                    j: usize
                }
                boxes[j - 1].insert(i);
                cards[i - 1].insert(j);
            }
            2 => {
                input! {
                    i: usize,
                }
                let ans = boxes[i - 1]
                    .iter()
                    .map(|&j| repeat(&j.to_string(), cards[j - 1].count(&i), " "))
                    .collect::<Vec<_>>()
                    .join(" ");
                println!("{}", ans);
            }
            3 => {
                input! {
                    i: usize,
                }
                let ans = cards[i - 1]
                    .iter()
                    .map(|&j| j.to_string())
                    .collect::<Vec<_>>()
                    .join(" ");
                println!("{}", ans);
            }
            _ => unreachable!(),
        }
    }
}

#[derive(Debug, Clone)]
struct MultiSet<T>
where
    T: Ord + Hash + Clone,
{
    set: BTreeSet<T>,
    map: HashMap<T, usize>,
}

impl<T> MultiSet<T>
where
    T: Ord + Hash + Clone,
{
    fn new() -> Self {
        Self {
            set: BTreeSet::new(),
            map: HashMap::new(),
        }
    }

    fn insert(&mut self, value: T) {
        let key = value.clone();
        *self.map.entry(key).or_insert(0) += 1;
        self.set.insert(value);
    }

    fn remove(&mut self, value: T) {
        if let Some(x) = self.map.get_mut(&value) {
            *x -= 1;
            if *x == 0 {
                self.map.remove(&value);
            }
        }
    }

    fn contains(&self, value: &T) -> bool {
        self.map.contains_key(value)
    }

    fn is_empty(&self) -> bool {
        self.map.is_empty()
    }

    fn len(&self) -> usize {
        self.map.len()
    }

    fn count(&self, value: &T) -> usize {
        *self.map.get(value).unwrap_or(&0)
    }

    fn iter(&self) -> impl Iterator<Item = &T> {
        self.set.iter()
    }
}
