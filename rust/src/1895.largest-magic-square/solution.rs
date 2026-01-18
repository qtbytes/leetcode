// Created by none at 2026/01/18 11:41
// leetgo: dev
// https://leetcode.com/problems/largest-magic-square/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::hash::RandomState;
use std::io::Cursor;
use std::mem::swap;

impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let max_k = min(m, n);

        let check = |k: usize| -> bool {
            // enumerate the start point
            for x in 0..m - k {
                for y in 0..n - k {
                    // dbg!(x, y, k);
                    let inner_check = |x: usize, y: usize| -> bool {
                        // check row
                        let row_sum = (0..=k).map(|j| grid[x][y + j]).sum::<i32>();
                        for i in 1..=k {
                            let cur_sum = (0..=k).map(|j| grid[x + i][y + j]).sum::<i32>();
                            if cur_sum != row_sum {
                                return false;
                            }
                        }

                        // check col
                        let col_sum = (0..=k).map(|i| grid[x + i][y]).sum::<i32>();
                        if col_sum != row_sum {
                            return false;
                        }
                        for j in 1..=k {
                            let cur_sum = (0..=k).map(|i| grid[x + i][y + j]).sum::<i32>();
                            if cur_sum != col_sum {
                                return false;
                            }
                        }

                        // check diagnoal
                        let diagnoal_sum: i32 = (0..=k).map(|i| grid[x + i][y + i]).sum();
                        if diagnoal_sum != row_sum {
                            return false;
                        }

                        // check anti-diagnoal
                        let anti_diagnoal_sum: i32 = (0..=k).map(|i| grid[x + i][y + k - i]).sum();
                        anti_diagnoal_sum == row_sum
                    };

                    if inner_check(x, y) {
                        return true;
                    }
                }
            }

            false
        };

        for k in (1..max_k).rev() {
            if check(k) {
                return k as i32 + 1;
            }
        }

        1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::largest_magic_square(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
