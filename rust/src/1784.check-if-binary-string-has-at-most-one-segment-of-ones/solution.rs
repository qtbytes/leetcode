// Created by none at 2026/03/06 12:53
// leetgo: dev
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        let x: i128 = i128::from_str_radix(&s, 2).unwrap();
        let low_bit = x & -x;
        let y = x + low_bit;
        y & (y - 1) == 0
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::check_ones_segment(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
