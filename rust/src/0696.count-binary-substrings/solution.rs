// Created by none at 2026/02/19 13:03
// leetgo: dev
// https://leetcode.com/problems/count-binary-substrings/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let mut pre = 0;
        let mut cnt = 1;
        let a = s.as_bytes();

        let mut res = 0;
        for i in 1..a.len() {
            if a[i] == a[i - 1] {
                cnt += 1
            } else {
                res += min(pre, cnt);
                pre = cnt;
                cnt = 1;
            }
        }
        res + min(pre, cnt)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::count_binary_substrings(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
