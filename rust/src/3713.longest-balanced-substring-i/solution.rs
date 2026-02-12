// Created by none at 2026/02/12 17:07
// leetgo: dev
// https://leetcode.com/problems/longest-balanced-substring-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;
use serde::de::IntoDeserializer;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let a = s.as_bytes();
        let n = s.len();
        let mut res = 0;
        for i in 0..n {
            if n - i < res {
                break;
            }
            let mut freq = vec![0; 26];
            let mut cnt = HashMap::new();
            for j in i..n {
                let x = (a[j] - b'a') as usize;
                freq[x] += 1;
                *cnt.entry(freq[x]).or_insert(0) += 1;
                if freq[x] > 1 {
                    *cnt.entry(freq[x] - 1).or_insert(0) -= 1;
                    if cnt[&(freq[x] - 1)] == 0 {
                        cnt.remove(&(freq[x] - 1));
                    }
                }
                if cnt.len() == 1 {
                    res = max(res, j - i + 1)
                }
            }
        }

        res as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::longest_balanced(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
