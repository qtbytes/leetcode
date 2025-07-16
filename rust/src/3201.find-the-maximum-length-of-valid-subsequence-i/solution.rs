// Created by none at 2025/07/16 10:29
// leetgo: dev
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        fn find(nums: &Vec<i32>, last: i32, target: i32) -> i32 {
            let mut res = 0;
            let mut last = last;
            for &x in nums {
                let x = x & 1;
                if x ^ last == target {
                    res += 1;
                    last = x;
                }
            }
            res
        }

        find(&nums, 0, 1)
            .max(find(&nums, 1, 1))
            .max(find(&nums, 0, 0))
            .max(find(&nums, 1, 0))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_length(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
