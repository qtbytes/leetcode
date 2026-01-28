// Created by none at 2026/01/28 12:09
// leetgo: dev
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::iter::Rev;
use std::mem::swap;

impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>, max_k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let max_k = max_k as usize;
        let mut f = vec![vec![vec![1e9 as i32; n + 1]; m + 1]; max_k + 1];
        for k in 0..=max_k {
            // we should maintain a sorted map
            // index is increasing, value is increasing
            let mut map: BTreeMap<i32, i32> = BTreeMap::new();
            if k > 0 {
                for i in 0..m {
                    for j in 0..n {
                        let v = f[k - 1][i + 1][j + 1];
                        let mut to_move = vec![];
                        for (&key, &value) in map.range(..=grid[i][j]).rev() {
                            if value >= v {
                                to_move.push(key);
                            } else {
                                break;
                            }
                        }
                        for key in to_move {
                            map.remove(&key);
                        }
                        if let Some((_, &value)) = map.range(grid[i][j]..).next() {
                            if value > v {
                                map.insert(grid[i][j], v);
                            }
                        } else {
                            map.insert(grid[i][j], v);
                        }
                    }
                }
            }
            // println!("{:?}", map);
            f[k][1][1] = 0;
            for i in 0..m {
                for j in 0..n {
                    // normal move
                    f[k][i + 1][j + 1] = min(
                        f[k][i + 1][j + 1],
                        min(f[k][i][j + 1], f[k][i + 1][j]) + grid[i][j],
                    );
                    // teleportation
                    if k > 0 {
                        if let Some((_, &value)) = map.range(grid[i][j]..).next() {
                            f[k][i + 1][j + 1] = min(f[k][i + 1][j + 1], value);
                        }
                    }
                }
            }
            // println!("{:?}", f[k]);
        }
        f[max_k][m][n]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_cost(grid, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
