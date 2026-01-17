// Created by none at 2026/01/17 14:09
// leetgo: dev
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let n = bottom_left.len();

        let mut max_l = 0;

        let calc = |i: usize, j: usize| -> i32 {
            let x1 = max(bottom_left[i][0], bottom_left[j][0]);
            let y1 = max(bottom_left[i][1], bottom_left[j][1]);
            let x2 = min(top_right[i][0], top_right[j][0]);
            let y2 = min(top_right[i][1], top_right[j][1]);

            if x1 >= x2 || y1 >= y2 {
                0
            } else {
                (x2 - x1).min(y2 - y1)
            }
        };

        for i in 0..n {
            let l = top_right[i][0] - bottom_left[i][0];
            if l <= max_l {
                continue;
            }
            for j in 0..i {
                // check the intersecting region of rec[i] and rec[j]
                max_l = max(max_l, calc(i, j))
            }
        }

        max_l as i64 * max_l as i64
    }
}

// @lc code=end

fn main() -> Result<()> {
    let bottom_left: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let top_right: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::largest_square_area(bottom_left, top_right).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
