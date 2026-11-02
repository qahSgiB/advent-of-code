use std::fs;


fn main() {
    let s = fs::read_to_string("input.txt").unwrap();
    let heights: Vec<i32> = s.split('\n').map(|s| s.parse().unwrap()).collect();
}
