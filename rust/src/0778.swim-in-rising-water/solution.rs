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
    pub fn swim_in_water(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut q = BinaryHeap::new();
        fn add(
            q: &mut BinaryHeap<(i32, usize, usize)>,
            x: usize,
            y: usize,
            grid: &mut Vec<Vec<i32>>,
        ) {
            if grid[x][y] == -1 {
                return;
            }
            q.push((-grid[x][y], x, y));
            grid[x][y] = -1;
        }
        add(&mut q, 0, 0, &mut grid);
        let dirs = [0, 1, 0, -1, 0];
        let mut res = 0;
        while let Some((t, i, j)) = q.pop() {
            res = res.max(-t);
            if (i, j) == (n - 1, n - 1) {
                return res;
            }
            for d in 0..4 {
                let (x, y) = (i as i32 + dirs[d], j as i32 + dirs[d + 1]);
                if 0 <= x && x < n as i32 && 0 <= y && y < n as i32 {
                    add(&mut q, x as usize, y as usize, &mut grid);
                }
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
