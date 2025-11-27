// Created by none at 2025/11/27 20:23
// leetgo: dev
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut prefix_min = vec![1e15 as i64; k];
        let mut res = i64::MIN;
        let mut s = 0;

        for (i, &x) in nums.iter().enumerate() {
            let x = x as i64;
            let j = (i + 1) % k; // group sum by (divide k)
            s += x;
            res = max(res, s - prefix_min[j]);
            if j == 0 {
                res = max(res, s)
            }
            prefix_min[j] = min(prefix_min[j], s)
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::max_subarray_sum(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
