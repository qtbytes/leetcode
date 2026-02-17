// Created by none at 2026/02/17 10:26
// leetgo: dev
// https://leetcode.com/problems/binary-watch/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::fmt::format;
use std::mem::swap;

impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut res = vec![];
        for h in 0_i32..12 {
            let cnt = h.count_ones();
            if cnt > turned_on as u32 {
                continue;
            }
            for m in 0_i32..60 {
                let total = cnt + m.count_ones();
                if total == turned_on as u32 {
                    res.push(format!("{:}:{:02}", h, m));
                }
            }
        }
        // dbg!(&res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let turned_on: i32 = deserialize(&read_line()?)?;
    let ans: Vec<String> = Solution::read_binary_watch(turned_on).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
