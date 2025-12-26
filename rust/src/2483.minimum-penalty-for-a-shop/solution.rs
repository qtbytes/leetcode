// Created by none at 2025/12/26 19:33
// leetgo: dev
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let mut t = 0;
        let mut p = customers.chars().filter(|&ch| ch == 'Y').count();
        let mut min_p = p;

        let mut left = 0;

        for (i, ch) in customers.char_indices() {
            // close at i+1
            if ch == 'N' {
                left += 1
            } else {
                p -= 1
            }
            if left + p < min_p {
                min_p = left + p;
                t = i + 1
            }
        }

        t as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let customers: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::best_closing_time(customers).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
