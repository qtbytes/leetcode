// Created by none at 2026/02/22 20:25
// leetgo: dev
// https://leetcode.com/problems/binary-gap/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn binary_gap(mut n: i32) -> i32 {
        let mut has_one = false;
        let mut cnt = 0;
        let mut res = 0;

        while n > 0 {
            if n & 1 == 1 {
                if has_one {
                    res = max(res, cnt);
                }
                has_one = true;
                cnt = 0;
            }
            cnt += 1;
            n >>= 1;
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::binary_gap(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
