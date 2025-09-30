// Created by none at 2025/09/30 21:53
// leetgo: dev
// https://leetcode.com/problems/majority-frequency-characters/
// https://leetcode.com/contest/biweekly-contest-166/problems/majority-frequency-characters/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn majority_frequency_group(s: String) -> String {
        let mut cnt: HashMap<char, i32> = HashMap::new();
        for ch in s.chars() {
            *cnt.entry(ch).or_default() += 1;
        }

        let mut freq: HashMap<i32, Vec<char>> = HashMap::new();
        for (&ch, &f) in &cnt {
            freq.entry(f).or_default().push(ch);
        }

        let mut max_size = 0;
        let mut max_f = 0;
        let mut res = &vec![];

        for (&f, v) in &freq {
            if (v.len(), f) > (max_size, max_f) {
                (max_size, max_f) = (v.len(), f);
                res = v;
            }
        }

        res.into_iter().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: String = Solution::majority_frequency_group(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
