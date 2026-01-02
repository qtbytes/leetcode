// Created by none at 2026/01/02 13:41
// leetgo: dev
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn repeated_n_times(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len() / 2;

        if nums[1] == nums[0] || nums[1] == nums[2] {
            return nums[1];
        }
        nums[n + 1]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::repeated_n_times(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
