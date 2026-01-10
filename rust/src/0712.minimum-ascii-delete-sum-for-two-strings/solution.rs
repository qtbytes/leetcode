// Created by none at 2026/01/10 16:39
// leetgo: dev
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        // first, we should find the longest common sequence,
        // since delete one char is always cheaper than delete two,
        // at the same time, maintain delete prices for each sub sequence
        let a: Vec<char> = s1.chars().collect();
        let b: Vec<char> = s2.chars().collect();

        let m = a.len();
        let n = b.len();

        // let mut f = vec![vec![0; n + 1]; m + 1];
        let mut sum = vec![vec![0; n + 1]; m + 1];

        for i in 0..m {
            for j in 0..n {
                // f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1]);
                sum[i + 1][j + 1] = max(sum[i + 1][j], sum[i][j + 1]);
                if a[i] == b[j] {
                    // f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1);
                    sum[i + 1][j + 1] = max(sum[i + 1][j + 1], sum[i][j] + a[i] as i32)
                }
            }
        }

        let total: i32 = a.iter().chain(&b).map(|&x| x as i32).sum();
        total - 2 * sum[m][n]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s1: String = deserialize(&read_line()?)?;
    let s2: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_delete_sum(s1, s2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
