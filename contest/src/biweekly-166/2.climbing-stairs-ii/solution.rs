// Created by none at 2025/09/30 21:53
// leetgo: dev
// https://leetcode.com/problems/climbing-stairs-ii/
// https://leetcode.com/contest/biweekly-contest-166/problems/climbing-stairs-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

const INF: i32 = 1e9 as i32;

impl Solution {
    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut f = vec![INF; n + 1];

        f[0] = 0;
        for i in 1..=n {
            for j in 1..=3 {
                if i >= j {
                    f[i] = f[i].min(costs[i - 1] + f[i - j] + j as i32 * j as i32);
                }
            }
        }
        f[n]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let costs: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::climb_stairs(n, costs).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
