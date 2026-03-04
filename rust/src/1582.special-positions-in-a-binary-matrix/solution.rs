// Created by none at 2026/03/04 13:17
// leetgo: dev
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();

        let mut row = vec![0; m];
        let mut col = vec![0; n];
        for i in 0..m {
            for j in 0..n {
                row[i] += mat[i][j];
                col[j] += mat[i][j];
            }
        }

        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 && row[i] == 1 && col[j] == 1 {
                    res += 1;
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mat: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_special(mat).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
