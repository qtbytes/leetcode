// Created by none at 2026/03/20 16:14
// leetgo: dev
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn calculate_min_diff(nums: &BTreeMap<i32, i32>) -> i32 {
    // dbg!(nums);
    let mut res = i32::MAX;
    let mut pre = None;
    for x in nums.keys() {
        if let Some(y) = pre {
            res = min(res, x - y)
        }
        pre = Some(x)
    }
    // if only have one key, the diff is 0
    if res == i32::MAX { 0 } else { res }
}

impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let k = k as usize;

        // calculate the first matrix

        let mut nums = BTreeMap::new();
        for i in 0..k {
            for j in 0..k {
                *nums.entry(grid[i][j]).or_insert(0) += 1;
            }
        }

        let mut res = vec![vec![0; n - k + 1]; m - k + 1];
        for top in 0..=m - k {
            // copy the first martix to move down
            let tmp = nums.clone();
            res[top][0] = calculate_min_diff(&nums);
            for left in 1..=n - k {
                // move matrix to right, only infect column left and left + k - 1
                for row in top..top + k {
                    *nums.entry(grid[row][left + k - 1]).or_insert(0) += 1;
                    *nums.entry(grid[row][left - 1]).or_insert(0) -= 1;
                    // remove 0 count keys
                    if nums.get(&grid[row][left - 1]).unwrap() == &0 {
                        nums.remove(&grid[row][left - 1]);
                    }
                }
                res[top][left] = calculate_min_diff(&nums);
            }

            if top + k >= m {
                break;
            }
            // move matrix down, only infect row top and top + k - 1
            nums = tmp;
            for col in 0..k {
                *nums.entry(grid[top + k][col]).or_insert(0) += 1;
                *nums.entry(grid[top][col]).or_insert(0) -= 1;
                // remove 0 count keys
                if nums.get(&grid[top][col]).unwrap() == &0 {
                    nums.remove(&grid[top][col]);
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
    let ans: Vec<Vec<i32>> = Solution::min_abs_diff(grid, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
