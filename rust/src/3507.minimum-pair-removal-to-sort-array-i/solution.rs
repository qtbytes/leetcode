// Created by none at 2026/01/22 13:32
// leetgo: dev
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn check(nums: &Vec<i32>) -> bool {
    nums.windows(2).all(|w| w[0] <= w[1])
}

fn operate(mut nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut j = 0;
    let mut sum = nums[j] + nums[j + 1];

    for i in 1..n - 1 {
        let cur_sum = nums[i] + nums[i + 1];
        if cur_sum < sum {
            sum = cur_sum;
            j = i
        }
    }
    nums[j] = sum;
    nums.remove(j + 1);
    nums
}

impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        if check(&nums) {
            0
        } else {
            1 + Self::minimum_pair_removal(operate(nums))
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_pair_removal(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
