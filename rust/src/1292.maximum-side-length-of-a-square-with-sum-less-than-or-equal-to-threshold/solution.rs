// Created by none at 2026/01/19 13:02
// leetgo: dev
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let m = mat.len();
        let n = mat[0].len();

        let mut max_l = 0;

        let mut f = vec![vec![0; n + 1]; m + 1]; //prefix sum
        for i in 0..m {
            for j in 0..n {
                // calculate prefix sum
                f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1] - f[i][j] + mat[i][j];

                // use (i,j) as bottom-right of square
                // early stop
                if min(i + 1, j + 1) <= max_l {
                    continue;
                }
                // use binary serach to speed up
                let mut l = 0;
                let mut r = min(i + 1, j + 1);

                while l < r {
                    let mid = (l + r + 1) >> 1;
                    // top-left
                    let (x, y) = (i + 1 - mid, j + 1 - mid);
                    let sum = f[i + 1][j + 1] - f[i + 1][y] - f[x][j + 1] + f[x][y];
                    if sum <= threshold {
                        l = mid
                    } else {
                        r = mid - 1
                    }
                }

                max_l = max(max_l, l)
            }
        }

        max_l as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mat: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let threshold: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_side_length(mat, threshold).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
