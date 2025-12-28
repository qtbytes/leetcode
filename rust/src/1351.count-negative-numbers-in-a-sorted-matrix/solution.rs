// Created by none at 2025/12/28 11:17
// leetgo: dev
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;

        let mut j = 0;

        for i in (0..m).rev() {
            while j < n && grid[i][j] >= 0 {
                j += 1
            }
            ans += n - j;
        }

        ans as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::count_negatives(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
