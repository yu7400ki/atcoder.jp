#![allow(dead_code)]
use proconio::{fastout, input};
use itertools::Itertools;
use std::f64::consts::PI;


#[derive(Debug, Copy, Clone)]
struct Vec2d {
    x: f64,
    y: f64,
}

impl Vec2d {
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    fn add(self, other: Self) -> Self {
        Self::new(self.x + other.x, self.y + other.y)
    }

    fn sub(self, other: Self) -> Self {
        Self::new(self.x - other.x, self.y - other.y)
    }

    fn norm(self) -> f64 {
        self.x * self.x + self.y * self.y
    }

    fn abs(self) -> f64 {
        self.norm().sqrt()
    }

    fn dot(self, other: Self) -> f64 {
        self.x * other.x + self.y * other.y
    }
}

impl std::ops::Add for Vec2d {
    type Output = Self;
    fn add(self, other: Self) -> Self {
        self.add(other)
    }
}

impl std::ops::Sub for Vec2d {
    type Output = Self;
    fn sub(self, other: Self) -> Self {
        self.sub(other)
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        xy: [(f64, f64); n],
    }

    let xy = xy.into_iter().map(|(x, y)| Vec2d::new(x, y)).collect::<Vec<_>>();

    let mut ans = 0.;
    for it in (0..n).permutations(3) {
        let p_i = xy[it[0]];
        let p_j = xy[it[1]];
        let p_k = xy[it[2]];
        let u = p_j - p_i;
        let v = p_k - p_i;
        let cos = u.dot(v) / (u.abs() * v.abs());
        let deg = cos.acos() * 180.0 / PI;
        if deg > ans {
            ans = deg;
        }
    }

    println!("{}", ans);
}
