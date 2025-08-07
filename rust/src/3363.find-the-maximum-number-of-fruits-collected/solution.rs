// Created by none at 2025/08/07 12:25
// leetgo: dev
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

// Right { dx: usize, dy: usize },
// Down { dx: usize, dy: usize },
// TopRight { dx: usize, dy: usize },
// DownRight { dx: usize, dy: usize },
// DownLeft { dx: usize, dy: usize },
type Dirs = (usize, usize);

impl Solution {
    pub fn max_collected_fruits(fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();
        let mut fruits = fruits;

        fn dfs(
            x: usize,
            y: usize,
            dirs: &Vec<Dirs>,
            fruits: &Vec<Vec<i32>>,
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            let n = fruits.len();
            if !(x < n && y < n) || x > y {
                return i32::MIN;
            }
            if x == n - 1 {
                return if y == n - 1 { 0 } else { i32::MIN };
            }
            if memo[x][y] != i32::MIN {
                return memo[x][y];
            }
            let mut res = i32::MIN;
            for d in dirs {
                let (nx, ny) = (x.wrapping_add(d.0), y.wrapping_add(d.1));
                let next = dfs(nx, ny, dirs, fruits, memo);
                if next > res {
                    res = next;
                }
            }
            memo[x][y] = res + fruits[x][y];
            memo[x][y]
        }

        // top-left go first
        // only down-right
        let mut res = 0;
        for i in 0..n {
            res += fruits[i][i];
            fruits[i][i] = 0;
        }

        let mut memo = vec![vec![i32::MIN; n]; n];
        // top-right go second
        // down_left down down_right
        let dirs = vec![(1, usize::MAX), (1, 0), (1, 1)];
        res += dfs(0, n - 1, &dirs, &fruits, &mut memo);

        // down-left go third
        // reverse to top-right
        for i in 0..n {
            for j in i + 1..n {
                fruits[i][j] = fruits[j][i];
                memo[i][j] = i32::MIN;
            }
        }
        res += dfs(0, n - 1, &dirs, &fruits, &mut memo);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let fruits: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_collected_fruits(fruits).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
