// Created by none at 2025/08/23 12:30
// leetgo: dev
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

#[derive(Debug, Clone, Copy)]
struct Point {
    x: usize,
    y: usize,
}

impl Solution {
    pub fn minimum_sum(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());

        fn dfs(p1: Point, p2: Point, cnt: usize, grid: &Vec<Vec<i32>>) -> i32 {
            assert!(p1.x <= p2.x && p1.y <= p2.y);
            if cnt == 1 {
                return Solution::minimum_area(&grid, p1, p2);
            }
            let mut res = i32::MAX;
            // try to split horizontal
            for i in p1.x..p2.x {
                // p1.....
                // .....p3 (split here)
                // p4.....
                // .....p2
                let p3 = Point { x: i, y: p2.y };
                let p4 = Point { x: i + 1, y: p1.y };

                res = res.min(dfs(p1, p3, 1, grid) + dfs(p4, p2, cnt - 1, grid));
                if cnt == 3 {
                    res = res.min(dfs(p1, p3, cnt - 1, grid) + dfs(p4, p2, 1, grid))
                }
            }

            // try to split vertical
            for j in p1.y..p2.y {
                //   j (split here)
                // p1.p4..
                // .......
                // .......
                // .p3..p2
                let p3 = Point { x: p2.x, y: j };
                let p4 = Point { x: p1.x, y: j + 1 };

                res = res.min(dfs(p1, p3, 1, grid) + dfs(p4, p2, cnt - 1, grid));
                if cnt == 3 {
                    res = res.min(dfs(p1, p3, cnt - 1, grid) + dfs(p4, p2, 1, grid))
                }
            }
            res
        }

        dfs(Point { x: 0, y: 0 }, Point { x: m - 1, y: n - 1 }, 3, &grid)
    }

    pub fn minimum_area(grid: &Vec<Vec<i32>>, start: Point, end: Point) -> i32 {
        // top-left of rectangle
        let mut p1 = end;
        // bot-right of rectangle
        let mut p2 = start;

        for i in start.x..=end.x {
            for j in start.y..=end.y {
                if grid[i][j] == 1 {
                    p1.x = p1.x.min(i);
                    p1.y = p1.y.min(j);
                    p2.x = p2.x.max(i);
                    p2.y = p2.y.max(j);
                }
            }
        }

        if p2.x < p1.x || p2.y < p1.y {
            0
        } else {
            let res = (p2.x + 1 - p1.x) * (p2.y + 1 - p1.y);
            res as i32
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_sum(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
