// Created by none at 2025/07/31 12:26
// leetgo: dev
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn subarray_bitwise_o_rs(arr: Vec<i32>) -> i32 {
        let mut res = HashSet::new();
        let mut prev = HashSet::new();

        for &x in &arr {
            prev.insert(0); // x | 0 == x
            let mut next = HashSet::new();
            for &y in prev.iter() {
                res.insert(x | y);
                next.insert(x | y);
            }
            prev = next
        }

        res.len() as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let arr: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::subarray_bitwise_o_rs(arr).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
