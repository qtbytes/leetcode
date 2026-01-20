// Created by none at 2026/01/20 14:21
// leetgo: dev
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![-1; n];

        // x is prime, the last bit is 1
        // we should find the last continue 1's
        // 10001111
        // 1111 -> 0111 + 1000
        for (i, mut x) in nums.into_iter().enumerate() {
            if x == 2 {
                continue;
            }
            let mut cnt = 0;
            while x & 1 == 1 {
                cnt += 1;
                x >>= 1;
            }
            let high = x << cnt;
            let low = (1 << (cnt - 1)) - 1;
            ans[i] = high | low;
        }

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::min_bitwise_array(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
