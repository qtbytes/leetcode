// Created by none at 2025/07/16 10:29
// leetgo: dev
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let b: Vec<i32> = nums.into_iter().map(|x| x & 1).collect();
        let mut f = vec![vec![0; 3]; n];
        // (0,1) | (1,0)
        // 1,1
        // 0,0
        let target = vec![1, 0, 0];
        let mut last: Vec<Option<usize>> = vec![None; 3];

        let mut res = 0;

        for (i, x) in b.iter().enumerate() {
            for j in 0..3 {
                if let Some(k) = last[j] {
                    if x ^ b[k] == target[j] {
                        f[i][j] = f[k][j] + 1;
                        last[j] = Some(i);
                    }
                } else {
                    if j == 0 || j & 1 == *x as usize {
                        last[j] = Some(i);
                        f[i][j] = 1
                    }
                }
                res = res.max(f[i][j])
            }
        }

        // println!("{:?}", f);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_length(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
