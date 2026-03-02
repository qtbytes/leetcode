// Created by none at 2026/03/02 10:38
// leetgo: dev
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 1 {
            return 0;
        }
        let mut cnt = vec![];
        for i in 0..n {
            if let Some(j) = (0..n).rev().find(|&j| grid[i][j] == 1) {
                cnt.push(n - j - 1);
            } else {
                cnt.push(n);
            }
        }
        if cnt.len() < n - 1 {
            return -1;
        }
        // so we should find the least swap time to `sort` rows
        // just find the first valid and replace will be ok
        let mut res = 0;
        for i in 0..cnt.len() {
            let zero_need = n - 1 - i;
            if cnt[i] < zero_need {
                if let Some(j) = (i + 1..cnt.len()).find(|index| cnt[*index] >= zero_need) {
                    // move j to i
                    res += j - i;
                    for k in (i + 1..=j).rev() {
                        (cnt[k], cnt[k - 1]) = (cnt[k - 1], cnt[k]);
                    }
                } else {
                    return -1;
                }
            }
        }

        res as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_swaps(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
