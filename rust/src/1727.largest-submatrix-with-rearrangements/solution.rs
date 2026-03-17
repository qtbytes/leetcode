// Created by none at 2026/03/17 16:40
// leetgo: dev
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        let n = matrix[0].len();
        let mut h = vec![0; n];

        for row in matrix {
            for (i, &x) in row.iter().enumerate() {
                if x == 0 {
                    h[i] = 0
                } else {
                    h[i] += 1;
                }
            }
            let mut h_copy = h.clone();
            h_copy.sort_unstable_by_key(|x| -x);

            for i in 0..n {
                res = max(res, h_copy[i] * (i as i32 + 1))
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::largest_submatrix(matrix).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
