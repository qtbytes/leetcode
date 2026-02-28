// Created by none at 2026/02/28 10:40
// leetgo: dev
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

const MOD: i64 = 1e9 as i64 + 7;

impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        let mut res = 0;
        for i in 1..=n {
            let size = 32 - i.leading_zeros();
            res = ((res << size) | i as i64) % MOD
        }
        res as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::concatenated_binary(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
