// Created by none at 2025/09/27 09:54
// leetgo: dev
// https://leetcode.com/problems/largest-triangle-area/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
fn calc(a: &Vec<i32>, b: &Vec<i32>, c: &Vec<i32>) -> f64 {
    let s = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]);
    s.abs() as f64 / 2.0
}

impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        let mut res: f64 = 0.0;
        let n = points.len();
        for i in 0..n {
            for j in i + 1..n {
                for k in j + 1..n {
                    res = res.max(calc(&points[i], &points[j], &points[k]))
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let points: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: f64 = Solution::largest_triangle_area(points).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
