// Created by none at 2025/07/16 11:12
// leetgo: dev
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        if k == 1 {
            return nums.len() as _;
        }
        let k = k as usize;
        let mut dp = vec![vec![0; k]; k];

        for j in 0..k {
            for &x in &nums {
                let x = (x as usize) % k;
                let y = (j + k - x) % k;
                dp[j][x] = dp[j][x].max(1 + dp[j][y]);
                // assert!((x + y) % k == j);
            }
        }

        dp.into_iter()
            .map(|row| row.into_iter().max().unwrap())
            .max()
            .unwrap()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_length(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
