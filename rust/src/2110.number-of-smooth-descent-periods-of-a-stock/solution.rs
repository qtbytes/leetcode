// Created by none at 2025/12/15 12:43
// leetgo: dev
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut res = 0;

        let mut l = 0;
        for (r, &x) in prices.iter().enumerate() {
            if r == l || x + 1 == prices[r - 1] {
                continue;
            }
            let size = r - l;
            res += size * (size + 1) / 2;
            l = r
        }
        let size = prices.len() - l;
        res += size * (size + 1) / 2;
        res as i64
    }
}

// @lc code=end

fn main() -> Result<()> {
    let prices: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::get_descent_periods(prices).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
