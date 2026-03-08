// Created by none at 2026/03/08 14:13
// leetgo: dev
// https://leetcode.com/problems/find-unique-binary-string/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let mut seen = HashSet::new();
        let n = nums.len();
        for s in nums {
            let x = u32::from_str_radix(&s, 2).unwrap();
            seen.insert(x);
        }

        for x in 0..1 << n {
            if !seen.contains(&x) {
                return format!("{:0width$b}", x, width = n);
            }
        }

        unreachable!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<String> = deserialize(&read_line()?)?;
    let ans: String = Solution::find_different_binary_string(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
