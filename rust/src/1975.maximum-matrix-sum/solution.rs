// Created by none at 2026/01/05 14:27
// leetgo: dev
// https://leetcode.com/problems/maximum-matrix-sum/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::i64::MAX;
use std::mem::swap;

impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        // find the max neg and min pos
        // if count of neg is odd, then sub 2 * min(-neg, pos)

        let mut neg = i32::MIN;
        let mut pos = i32::MAX;
        let mut ans = 0;
        let mut cnt = 0;
        for row in matrix {
            for x in row {
                ans += x.abs() as i64;
                if x <= 0 {
                    cnt += 1;
                    neg = max(neg, x)
                } else {
                    pos = min(pos, x)
                }
            }
        }

        // println!("{neg} {pos} {cnt} ");
        if cnt & 1 == 1 {
            ans - 2 * min(-neg, pos) as i64
        } else {
            ans
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::max_matrix_sum(matrix).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
