// Created by none at 2025/07/25 12:29
// leetgo: dev
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();

        let n = nums.len();
        if nums[n - 1] <= 0 {
            return nums[n - 1];
        }

        let mut res = 0;
        for (i, &x) in nums.iter().enumerate() {
            if x <= 0 || (i > 0 && x == nums[i - 1]) {
                continue;
            }
            res += x;
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_sum(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
