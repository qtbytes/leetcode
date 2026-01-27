// Created by none at 2026/01/27 13:08
// leetgo: dev
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::iter::Rev;
use std::mem::swap;

impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![vec![]; n];
        for e in edges {
            let (x, y, cost) = (e[0] as usize, e[1] as usize, e[2]);
            g[x].push((y, cost));
            g[y].push((x, 2 * cost));
        }

        // shortest path
        let mut dist = vec![-1; n];
        dist[0] = 0;
        let mut h = BinaryHeap::new(); // (dist, index)
        h.push((Reverse(0), 0));
        while let Some((Reverse(d), x)) = h.pop() {
            if x == n - 1 {
                return d;
            }
            for &(y, cost) in &g[x] {
                if dist[y] == -1 || dist[y] > d + cost {
                    dist[y] = d + cost;
                    h.push((Reverse(dist[y]), y));
                }
            }
        }

        -1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let edges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_cost(n, edges).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
