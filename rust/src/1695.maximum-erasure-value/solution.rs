// Created by none at 2025/07/22 09:23
// leetgo: dev
// https://leetcode.com/problems/maximum-erasure-value/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut l = 0;
        let mut last = HashMap::new();
        let mut sum = 0;

        for (i, x) in nums.iter().enumerate() {
            sum += *x;
            if let Some(&j) = last.get(x) {
                while l <= j {
                    sum -= nums[l];
                    l += 1;
                }
            }
            last.insert(*x, i);
            res = res.max(sum)
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_unique_subarray(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
