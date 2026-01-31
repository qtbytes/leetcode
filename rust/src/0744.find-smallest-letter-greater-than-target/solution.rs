// Created by none at 2026/01/31 13:32
// leetgo: dev
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let i = letters.partition_point(|&ch| ch <= target);
        if i == letters.len() {
            letters[0]
        } else {
            letters[i]
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let letters: Vec<char> = deserialize(&read_line()?)?;
    let target: char = deserialize(&read_line()?)?;
    let ans: char = Solution::next_greatest_letter(letters, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
