// Created by none at 2025/10/21 10:40
// leetgo: dev
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        nums.sort_unstable();
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *cnt.entry(x).or_default() += 1;
        }

        let n = nums.len();
        let mut l = 0;
        let mut r = 0;
        let mut res = 0;
        for target in nums[0]..=nums[n - 1] {
            while nums[l] + k < target {
                l += 1;
            }
            while r < n && nums[r] - k <= target {
                r += 1;
            }
            let equal = cnt.get(&target).unwrap_or(&0);
            res = max(res, equal + min((r - l) as i32 - (equal), num_operations));
        }

        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let num_operations: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_frequency(nums, k, num_operations).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
