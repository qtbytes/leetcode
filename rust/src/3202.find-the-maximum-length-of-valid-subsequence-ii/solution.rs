// Created by none at 2025/07/16 11:12
// leetgo: dev
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if k == 1 {
            return n as _;
        }
        let mut idx = vec![vec![]; k as usize];
        nums.into_iter().enumerate().for_each(|(i, x)| {
            idx[(x % k) as usize].push(i);
        });

        let mut res = idx.iter().map(|v| v.len()).max().unwrap();

        for (x, a) in idx.iter().enumerate() {
            if a.is_empty() {
                continue;
            }

            for y in x + 1..idx.len() {
                let b = &idx[y];
                if b.is_empty() {
                    continue;
                }
                let mut i = 0;
                let mut j = 0;
                let mut cur = 1;
                let mut flg = 0b11;
                while i < a.len() && j < b.len() {
                    if a[i] < b[j] {
                        i += 1;
                        if flg & 1 != 0 {
                            flg = 0b10;
                            cur += 1;
                        }
                    } else {
                        j += 1;
                        if flg & 0b10 != 0 {
                            flg = 1;
                            cur += 1;
                        }
                    }
                }
                res = res.max(cur)
            }
        }

        res as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_length(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
