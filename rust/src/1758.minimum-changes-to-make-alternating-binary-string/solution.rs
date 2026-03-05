// Created by none at 2026/03/05 11:48
// leetgo: dev
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let a = s.as_bytes();
        let n = a.len();
        let mut res = 0;

        // let s became 010101
        for (i, x) in a.iter().enumerate() {
            if (x - b'0') as usize != i & 1 {
                res += 1;
            }
        }
        // s became 101010 need `n - res` times
        min(res, n - res) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_operations(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
