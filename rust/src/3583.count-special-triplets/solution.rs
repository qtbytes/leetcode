// Created by none at 2025/12/09 12:28
// leetgo: dev
// https://leetcode.com/problems/count-special-triplets/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::new();

        for (i, &x) in nums.iter().enumerate() {
            map.entry(x).or_insert(vec![]).push(i);
        }

        let mut ans = 0;
        let m = 1e9 as usize + 7;

        for j in 1..nums.len() - 1 {
            let x = nums[j];
            if let Some(v) = map.get(&(x * 2)) {
                let i = v.partition_point(|&i| i < j);
                let k = v.partition_point(|&i| i <= j);
                ans = (ans + (v.len() - k) * i) % m
            }
        }

        ans as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::special_triplets(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
