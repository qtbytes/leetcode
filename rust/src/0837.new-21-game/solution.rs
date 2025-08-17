// Created by none at 2025/08/17 09:17
// leetgo: dev
// https://leetcode.com/problems/new-21-game/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        // ```
        // Input: n = 21, k = 17, maxPts = 10
        // Output: 0.73278
        // ```
        // - `0 <= k <= n <= 10⁴`
        // - `1 <= maxPts <= 10⁴`

        if k + max_pts <= n {
            return 1.0;
        }
        let (n, k, m) = (n as usize, k as usize, max_pts as usize);
        // dp[i] = sum(dp[i+1, i+m+1]) / m

        let mut dp = vec![0.0; k + m + 1];
        for i in k..=n {
            dp[i] = 1.0
        }

        let mut sum: f64 = dp[k..k + m + 1].iter().sum();

        for i in (0..k).rev() {
            // dp[i] = dp[i + 1..i + 1 + m].iter().sum::<f64>() / m as f64;
            sum -= dp[i + m + 1];
            dp[i] = sum / (m as f64);
            sum += dp[i]
        }
        dp[0]

        // TLE
        // fn dfs(x: i32, n: i32, k: i32, max_pts: i32, memo: &mut Vec<f64>) -> f64 {
        //     if x >= k {
        //         return 1.0;
        //     }
        //     if memo[x as usize] != -1.0 {
        //         return memo[x as usize];
        //     }
        //     let mut res = 0.0;
        //     for y in 1..=max_pts.min(n - x) {
        //         res += dfs(x + y, n, k, max_pts, memo)
        //     }
        //     memo[x as usize] = res / (max_pts as f64);
        //     memo[x as usize]
        // }
        // let mut memo = vec![-1.0; n as usize + 1];
        // dfs(0, n, k, max_pts, &mut memo)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let max_pts: i32 = deserialize(&read_line()?)?;
    let ans: f64 = Solution::new21_game(n, k, max_pts).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
