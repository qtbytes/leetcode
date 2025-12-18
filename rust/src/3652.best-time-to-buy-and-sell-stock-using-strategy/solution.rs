// Created by none at 2025/12/18 13:59
// leetgo: dev
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::io::PipeReader;
use std::mem::swap;
use std::process::ExitStatus;

impl Solution {
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let n = prices.len();
        let mut profit = vec![0; n + 1];
        let mut prefix_price = vec![0; n + 1];

        for i in 0..n {
            profit[i + 1] = profit[i] + (prices[i] * strategy[i]) as i64;
            prefix_price[i + 1] = prefix_price[i] + (prices[i]) as i64;
        }

        let mut ans = profit[n];

        for i in k..=n {
            // change s[..i]
            let j = i - k;
            // sum(p[:j]) + sum(p[i:]) + sum(price[i-k/2:i])
            let cur = profit[j] + profit[n] - profit[i] + prefix_price[i] - prefix_price[i - k / 2];
            ans = max(ans, cur)
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let prices: Vec<i32> = deserialize(&read_line()?)?;
    let strategy: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::max_profit(prices, strategy, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
