// Created by none at 2026/01/24 14:53
// leetgo: dev
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        nums.sort_unstable();
        (0..n / 2).map(|i| nums[i] + nums[n - 1 - i]).max().unwrap()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_pair_sum(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
