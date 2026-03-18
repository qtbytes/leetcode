// Created by none at 2026/03/18 15:19
// leetgo: dev
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        // typical 2d prefix sum problem

        let m = grid.len();
        let n = grid[0].len();

        let mut f = vec![vec![0; n + 1]; m + 1];
        let mut res = 0;

        for (i, row) in grid.into_iter().enumerate() {
            for (j, x) in row.into_iter().enumerate() {
                f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1] + x - f[i][j];
                if f[i + 1][j + 1] <= k {
                    res += 1;
                } else {
                    break;
                }
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::count_submatrices(grid, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
