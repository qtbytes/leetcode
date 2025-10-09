// Created by none at 2025/10/09 12:05
// leetgo: dev
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let n = skill.len();
        let mut sum = vec![0; n + 1];

        for (i, &s) in skill.iter().enumerate() {
            sum[i + 1] = s as i64 + sum[i];
        }

        let mut pre_t = 0;
        let mut pre_m = 0;
        for m in mana {
            let m = m as i64;
            let mut t = pre_t + pre_m * sum[1]; // the first wizard
            for i in 0..n - 1 {
                t = max(t, pre_t + pre_m * sum[i + 2] - sum[i + 1] * m)
            }
            pre_t = t;
            pre_m = m;
        }
        pre_t + sum[n] * pre_m
    }
}

// @lc code=end

fn main() -> Result<()> {
    let skill: Vec<i32> = deserialize(&read_line()?)?;
    let mana: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::min_time(skill, mana).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
