// Created by none at 2025/10/15 09:51
// leetgo: dev
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        let mut pre_cnt = 0;
        let mut cnt = 1;
        let n = nums.len();
        let mut res = 0;
        for i in 1..n {
            if nums[i] > nums[i - 1] {
                cnt += 1;
            } else {
                pre_cnt = cnt;
                cnt = 1
            }
            res = max(res, max(cnt / 2, min(cnt, pre_cnt)))
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_increasing_subarrays(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
