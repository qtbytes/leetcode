// Created by none at 2025/12/30 12:44
// leetgo: dev
// https://leetcode.com/problems/magic-squares-in-grid/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut res = 0;
        let check = |i: usize, j: usize| -> bool {
            // check unique
            let mut seen = vec![false; 10];
            let mut row_sum = vec![0; 3];
            let mut col_sum = vec![0; 3];
            for r in i - 1..=i + 1 {
                for c in j - 1..=j + 1 {
                    let x = grid[r][c] as usize;
                    if x > 9 || seen[x] {
                        return false;
                    }
                    seen[x] = true;
                    row_sum[r - (i - 1)] += x;
                    col_sum[c - (j - 1)] += x;
                }
            }

            for i in 0..3 {
                if row_sum[i] != 15 || col_sum[i] != 15 {
                    return false;
                }
            }
            // no need to check both diagonals
            true
        };

        for i in 1..m - 1 {
            for j in 1..n - 1 {
                if grid[i][j] == 5 {
                    if check(i, j) {
                        res += 1
                    }
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_magic_squares_inside(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
