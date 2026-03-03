// Created by none at 2026/03/03 13:35
// leetgo: dev
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_kth_bit(_: i32, k: i32) -> char {
        let mut k = k as u32;
        let mut length = 1;
        let mut size = vec![];
        loop {
            size.push(length);
            length = 2 * length + 1;
            if length >= k {
                break;
            }
        }

        let mut flip = 0;
        while let Some(last) = size.pop() {
            // k is the left part
            if k <= last {
                continue;
            }
            // this bit must be 1
            if k == last + 1 {
                flip ^= 1;
                break;
            }
            flip ^= 1;
            k = 2 * (last + 1) - k;
        }

        // dbg!(&size, k, flip);

        ((flip as u8) + '0' as u8) as char
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: char = Solution::find_kth_bit(n, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
