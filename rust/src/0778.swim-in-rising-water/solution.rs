// Created by none at 2025/10/06 13:33
// leetgo: dev
// https://leetcode.com/problems/swim-in-rising-water/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut fa: Vec<usize> = (0..n * n).collect();

        fn find(x: usize, fa: &mut Vec<usize>) -> usize {
            if fa[x] != x {
                fa[x] = find(fa[x], fa)
            }
            fa[x]
        }

        fn union(x: usize, y: usize, fa: &mut Vec<usize>) -> bool {
            let (fx, fy) = (find(x, fa), find(y, fa));
            if fx == fy {
                return false;
            }
            fa[fy] = fx;
            true
        }

        let mut q = BinaryHeap::new();

        for (i, row) in grid.iter().enumerate() {
            for (j, &t) in row.iter().enumerate() {
                q.push((-t, i, j));
            }
        }

        let dirs = [0, -1, 0, 1, 0];
        while let Some((t, i, j)) = q.pop() {
            for d in 0..4 {
                let (x, y) = (i as i32 + dirs[d], j as i32 + dirs[d + 1]);
                if x >= 0 && x < n as i32 && y >= 0 && y < n as i32 {
                    if grid[x as usize][y as usize] < -t {
                        union(i * n + j, x as usize * n + y as usize, &mut fa);
                    }
                }
            }
            if find(0, &mut fa) == find(n * n - 1, &mut fa) {
                return -t;
            }
        }

        unreachable!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::swim_in_water(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
