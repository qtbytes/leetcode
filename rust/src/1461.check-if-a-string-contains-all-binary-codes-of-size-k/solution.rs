// Created by none at 2026/02/23 13:37
// leetgo: dev
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let a: Vec<i32> = s.as_bytes().iter().map(|x| (x - b'0') as i32).collect();
        let k = k as usize;
        let n = a.len();
        // n must have at least (1 << k) substring of size k
        if n < (1 << k) + (k - 1) {
            return false;
        }

        // sliding window
        let mut x: i32 = 0;
        for i in 0..k - 1 {
            x = (x << 1) | a[i]
        }
        let mut seen = HashSet::new();
        for i in k - 1..n {
            x = (x << 1) | a[i];
            seen.insert(x);
            x ^= (a[i - (k - 1)]) << (k - 1)
        }

        seen.len() == 1 << k
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: bool = Solution::has_all_codes(s, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
