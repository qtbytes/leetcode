// Created by none at 2025/10/18 11:23
// leetgo: dev
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_distinct_elements(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut last = nums[0] - k;
        let mut res = 0;
        for x in nums {
            if last < x - k {
                last = x - k + 1;
                res += 1;
            } else if last <= x + k {
                last += 1;
                res += 1;
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_distinct_elements(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
