// Created by none at 2025/11/30 14:42
// leetgo: dev
// https://leetcode.com/problems/make-sum-divisible-by-p/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let mut s = 0;
        for &x in &nums {
            s = (s + x) % p
        }
        // we need remove s
        let target = s;
        if target == 0 {
            return 0;
        }
        s = 0;

        let mut map = HashMap::new();
        map.insert(0, 0);
        let mut res = nums.len();

        for (i, &x) in nums.iter().enumerate() {
            let i = i + 1;
            s = (s + x) % p;
            if let Some(j) = map.get(&((s + p - target) % p)) {
                // delete nums[j..i]
                res = min(res, i - j)
            }
            map.insert(s, i);
        }

        if res == nums.len() { -1 } else { res as i32 }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let p: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_subarray(nums, p).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
