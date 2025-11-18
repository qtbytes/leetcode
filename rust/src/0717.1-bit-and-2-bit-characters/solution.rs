// Created by none at 2025/11/18 18:46
// leetgo: dev
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let n = bits.len();
        let mut f = vec![false; n + 1];

        f[n - 1] = true;

        for i in (0..n - 1).rev() {
            if bits[i] == 0 && f[i + 1] {
                f[i] = true;
            }
            if bits[i] == 1 && f[i + 2] {
                f[i] = true
            }
        }

        f[0]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let bits: Vec<i32> = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_one_bit_character(bits).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
