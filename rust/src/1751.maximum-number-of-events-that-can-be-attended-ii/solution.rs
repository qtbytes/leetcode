// Created by none at 2025/07/08 10:15
// leetgo: dev
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_value(events: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut events = events;
        let n = events.len();
        events.sort_unstable_by_key(|e| e[1]);

        // dp[i][j] = e[i][2] + max(dp[x][j-1]) if e[x][1] < e[i][0]
        let mut dp = vec![vec![0; k + 1]; n + 1];
        for (i, e) in events.iter().enumerate() {
            for j in 1..=k {
                let x = events[..i].partition_point(|event| event[1] < e[0]);
                dp[i + 1][j] = (dp[x][j - 1] + e[2]).max(dp[i][j]);
            }
        }
        // println!("{events:?}");
        // println!("{dp:?}");
        dp[n][k]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let events: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_value(events, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
