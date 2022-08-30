use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (ax, ay, bx, by, cx, cy, dx, dy): (i64, i64, i64, i64, i64, i64, i64, i64),
    }

    if in_triangle(ax, ay, bx, by, cx, cy, dx, dy) ||
        in_triangle(ax, ay, bx, by, dx, dy, cx, cy) || 
        in_triangle(ax, ay, dx, dy, cx, cy, bx, by) ||
        in_triangle(dx, dy, bx, by, cx, cy, ax, ay)
    {
        println!("No");
    }
    else
    {
        println!("Yes");
    }
    
}   


fn in_triangle(ax: i64, ay: i64, bx: i64, by: i64, cx: i64, cy: i64, px: i64, py: i64) -> bool {
    let c1: i64 = (bx - ax) * (py - ay) - (by - ay) * (px - ax);
    let c2: i64 = (cx - bx) * (py - by) - (cy - by) * (px - bx);
    let c3: i64 = (ax - cx) * (py - cy) - (ay - cy) * (px - cx);
    return c1 >= 0 && c2 >= 0 && c3 >= 0 || c1 < 0 && c2 < 0 && c3 < 0;
}