// Created by none at 2026/01/16 15:51
// leetgo: dev
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
fn handle(n: i32, mut fences: Vec<i32>) -> HashSet<i32> {
    fences.push(1);
    fences.push(n);
    fences.sort_unstable();

    let mut edges = HashSet::new();
    for i in 0..fences.len() {
        for j in 0..i {
            edges.insert(fences[i] - fences[j]);
        }
    }
    edges
}

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        let h = handle(m, h_fences);
        let v = handle(n, v_fences);

        let l = h.into_iter().filter(|e| v.contains(e)).max().unwrap_or(0) as i64;
        let area = (l * l) % (1e9 as i64 + 7);

        if area == 0 { -1 } else { area as i32 }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let m: i32 = deserialize(&read_line()?)?;
    let n: i32 = deserialize(&read_line()?)?;
    let h_fences: Vec<i32> = deserialize(&read_line()?)?;
    let v_fences: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximize_square_area(m, n, h_fences, v_fences).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
