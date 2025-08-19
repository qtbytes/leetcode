// Created by none at 2025/08/19 12:31
// leetgo: dev
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut cnt = 0;
        let mut res: i64 = 0;

        fn calc(cnt: i32) -> i64 {
            (1 + cnt as i64) * (cnt as i64) / 2
        }

        for x in nums {
            if x == 0 {
                cnt += 1;
            } else {
                res += calc(cnt);
                cnt = 0;
            }
        }

        // handle the last continue zeros: [0,0,0,2,0,0]
        res += calc(cnt);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::zero_filled_subarray(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
