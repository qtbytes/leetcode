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
        let mut prev = vec![];
        prev.push((0, 0));
        let mut dp = vec![vec![-1; k + 1]; n + 1];
        let mut res = 0;
        for j in 1..=k {
            let mut st = vec![];
            st.push((0, 0));
            for i in 0..n {
                let e = &events[i];
                let x = prev
                    .binary_search_by_key(&(e[0]), |&(_, r)| r)
                    .unwrap_or_else(|x| x)
                    - 1;
                dp[i + 1][j] = (prev[x].0 + e[2]).max(dp[i][j]);
                res = res.max(dp[i + 1][j]);
                while e[1] <= st.last().unwrap().1 {
                    st.pop();
                }
                st.push((dp[i + 1][j], e[1]));
                // assert!(dp[i + 1][j] >= dp[i + 1][j - 1])
            }
            prev = st;
        }
        // println!("{events:?}");
        // println!("{dp:?}");
        res
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
