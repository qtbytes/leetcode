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
        let mut pre = vec![0_i64; skill.len()];

        let mut t = 0;
        for (i, &s) in skill.iter().enumerate() {
            t += (mana[0] * s) as i64;
            pre[i] = t
        }

        for j in 1..mana.len() {
            let mut cur = vec![0_i64; skill.len()];

            let mut t = 0;
            for (i, &s) in skill.iter().enumerate() {
                t += (mana[j] * s) as i64;
                cur[i] = t;
            }

            t = pre[0];
            for i in 0..skill.len() - 1 {
                t = max(t, pre[i + 1] - cur[i])
            }
            for (i, &s) in skill.iter().enumerate() {
                t += (mana[j] * s) as i64;
                cur[i] = t;
            }
            pre = cur;
        }

        pre[skill.len() - 1]
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
