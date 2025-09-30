// Created by none at 2025/09/30 10:53
// leetgo: dev
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn triangular_sum(mut nums: Vec<i32>) -> i32 {
        for _ in 1..nums.len() {
            for i in 0..nums.len() - 1 {
                nums[i] = (nums[i] + nums[i + 1]) % 10
            }
            nums.pop();
        }
        nums[0] % 10
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::triangular_sum(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
