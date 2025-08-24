// Created by none at 2025/08/24 10:06
// leetgo: dev
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut r = 0;
        let mut res = 0;
        // previous subarray with all 1's
        let mut last: Option<(usize, usize)> = None;
        while r < n {
            if nums[r] == 0 {
                r += 1;
            } else {
                let l = r;
                while r < n && nums[r] == 1 {
                    r += 1;
                }
                res = res.max(r - l);
                if let Some((pl, pr)) = last {
                    if l - pr == 1 {
                        res = res.max(r - pl - 1)
                    }
                }
                last = Some((l, r));
            }
        }
        if res == n { res as i32 - 1 } else { res as i32 }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::longest_subarray(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
