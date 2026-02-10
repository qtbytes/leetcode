// Created by none at 2026/02/10 19:00
// leetgo: dev
// https://leetcode.com/problems/longest-balanced-subarray-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        // since `1 <= nums.length <= 1500`, so just enumerate l, r of subarray
        // time: O(n * n)
        // space: O(n)
        let mut max_length = 0;
        let n = nums.len();
        for i in 0..n {
            if i + max_length > n {
                break;
            }
            let mut cnt = vec![0; 2];
            let mut seen = HashSet::new();

            for j in i..n {
                if !seen.contains(&nums[j]) {
                    seen.insert(nums[j]);
                    cnt[(nums[j] & 1) as usize] += 1;
                }
                // we should check subarray whose size is greater than max_length
                if j - i >= max_length && cnt[0] == cnt[1] {
                    max_length = max(max_length, j - i + 1)
                }
            }
        }

        max_length as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::longest_balanced(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
