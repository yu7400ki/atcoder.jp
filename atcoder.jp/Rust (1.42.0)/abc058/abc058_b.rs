use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        o: String,
        e: String,
    }

    let ans = o.chars().zip(e.chars()).flat_map(|(o, e)| vec![o, e]).collect::<String>();
    if o.len() > e.len() {
        println!("{}{}", ans, o.chars().last().unwrap());
    } else {
        println!("{}", ans);
    }
}   
