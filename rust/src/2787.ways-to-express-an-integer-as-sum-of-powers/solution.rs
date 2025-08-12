// Created by none at 2025/08/12 16:44
// leetgo: dev
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
const MOD: i32 = 1e9 as i32 + 7;

impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        // - `1 <= n <= 300`
        // - `1 <= x <= 5`
        // worst case: x = 1, n = 300
        let n = n as usize;
        let x = x as u32;
        // find valid number
        let mut can: Vec<usize> = vec![];
        for i in 1..=n {
            if i.pow(x) <= n {
                can.push(i.pow(x));
            } else {
                break;
            }
        }

        // dp
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        for &number in &can {
            for target in (1..=n).rev() {
                if target >= number {
                    dp[target] += dp[target - number];
                    dp[target] %= MOD;
                }
            }
        }

        // println!("{can:?} {dp:?} ");
        dp[n]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let x: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::number_of_ways(n, x).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
