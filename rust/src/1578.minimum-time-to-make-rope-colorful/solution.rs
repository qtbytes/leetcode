// Created by none at 2025/11/03 18:16
// leetgo: dev
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let a = colors.as_bytes();
        let mut res = 0;
        let n = colors.len();
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            let mut max_t = needed_time[i];
            let mut total = needed_time[i];
            while j < n && a[j] == a[j - 1] {
                total += needed_time[j];
                max_t = max(max_t, needed_time[j]);
                j += 1;
            }
            res += total - max_t;
            i = j
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let colors: String = deserialize(&read_line()?)?;
    let needed_time: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_cost(colors, needed_time).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
