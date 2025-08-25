// Created by none at 2025/08/25 12:27
// leetgo: dev
// https://leetcode.com/problems/diagonal-traverse/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let (m, n) = (mat.len(), mat[0].len());
        let mut res = vec![];
        for s in 0..m + n - 1 {
            if s & 1 == 0 {
                let (mut x, mut y) = (s, 0);
                if x >= m {
                    (x, y) = (m - 1, s - (m - 1));
                }
                loop {
                    res.push(mat[x][y]);
                    if x.checked_sub(1).is_none() || y + 1 >= n {
                        break;
                    }
                    x -= 1;
                    y += 1;
                }
            } else {
                let (mut x, mut y) = (0, s);
                if y >= n {
                    (x, y) = (s - (n - 1), n - 1);
                }
                loop {
                    res.push(mat[x][y]);
                    if y.checked_sub(1).is_none() || x + 1 >= m {
                        break;
                    }
                    x += 1;
                    y -= 1;
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mat: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::find_diagonal_order(mat).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
