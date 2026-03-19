// Created by none at 2026/03/19 16:24
// leetgo: dev
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        // we use two 2d prefix sum
        // one for calculate +X-Y
        // one for X
        //

        let m = grid.len();
        let n = grid[0].len();
        let mut f = vec![vec![0; n + 1]; m + 1];
        let mut g = vec![vec![0; n + 1]; m + 1];
        let mut res = 0;

        for i in 0..m {
            for j in 0..n {
                let ch = grid[i][j];
                let x = match ch {
                    'X' => 1,
                    'Y' => -1,
                    _ => 0,
                };
                f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1] + x - f[i][j];
                let y = if ch == 'X' { 1 } else { 0 };
                g[i + 1][j + 1] = g[i + 1][j] + g[i][j + 1] + y - g[i][j];

                if f[i + 1][j + 1] == 0 && g[i + 1][j + 1] > 0 {
                    res += 1;
                }
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<char>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::number_of_submatrices(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
