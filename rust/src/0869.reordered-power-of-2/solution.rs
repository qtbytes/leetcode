// Created by none at 2025/08/10 12:26
// leetgo: dev
// https://leetcode.com/problems/reordered-power-of-2/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn count(n: i32) -> [i32; 10] {
    let mut n = n;
    let mut res = [0; 10];
    while n > 0 {
        res[(n % 10) as usize] += 1;
        n /= 10;
    }
    res
}

impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        let valid: HashSet<[i32; 10]> = HashSet::from_iter((0..31).map(|i| count(1 << i)));
        valid.contains(&count(n))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: bool = Solution::reordered_power_of2(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
