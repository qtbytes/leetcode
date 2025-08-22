// Created by none at 2025/08/22 13:31
// leetgo: dev
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

#[derive(Debug)]
struct Point {
    x: usize,
    y: usize,
}
impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        // top-left of rectangle
        let mut p1 = Point { x: m, y: n };
        // bot-right of rectangle
        let mut p2 = Point { x: 0, y: 0 };

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    p1.x = p1.x.min(i);
                    p1.y = p1.y.min(j);
                    p2.x = p2.x.max(i);
                    p2.y = p2.y.max(j);
                }
            }
        }
        // println!("{:?} {:?}", p1, p2);
        let res = (p2.x - p1.x + 1) * (p2.y - p1.y + 1);
        res as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_area(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
