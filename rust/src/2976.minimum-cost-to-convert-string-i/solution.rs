// Created by none at 2026/01/29 13:29
// leetgo: dev
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<char>,
        changed: Vec<char>,
        cost: Vec<i32>,
    ) -> i64 {
        let mut price = vec![vec![i32::MAX; 26]; 26];
        for i in 0..26 {
            price[i][i] = 0;
        }

        for (i, c) in cost.into_iter().enumerate() {
            let x = (original[i] as u8 - b'a') as usize;
            let y = (changed[i] as u8 - b'a') as usize;
            price[x][y] = min(price[x][y], c)
        }

        for k in 0..26 {
            for i in 0..26 {
                if price[i][k] == i32::MAX {
                    continue;
                }
                for j in 0..26 {
                    price[i][j] = min(price[i][j], price[i][k].saturating_add(price[k][j]))
                }
            }
        }

        let mut ans = 0;
        for (x, y) in source.bytes().zip(target.bytes()) {
            let x = (x - b'a') as usize;
            let y = (y - b'a') as usize;
            if price[x][y] == i32::MAX {
                return -1;
            }
            ans += price[x][y] as i64;
        }

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let source: String = deserialize(&read_line()?)?;
    let target: String = deserialize(&read_line()?)?;
    let original: Vec<char> = deserialize(&read_line()?)?;
    let changed: Vec<char> = deserialize(&read_line()?)?;
    let cost: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::minimum_cost(source, target, original, changed, cost).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
