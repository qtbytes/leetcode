// Created by none at 2026/03/16 14:49
// leetgo: dev
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn push(heap: &mut BinaryHeap<Reverse<i32>>, seen: &mut HashSet<i32>, val: i32) {
    if seen.contains(&val) {
        return;
    }
    seen.insert(val);
    heap.push(Reverse(val));
    if heap.len() > 3 {
        heap.pop();
    }
}

impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        // we maintain a max heap to store the top 3 rhombus sums
        // enumerate the top-left corner of each rhombus and calculate the sum
        // if the length is x, need 2 * x + 1 rows and columns to form the rhombus
        let m = grid.len();
        let n = grid[0].len();
        let mut heap = BinaryHeap::new();
        let mut seen = HashSet::new();

        for i in 0..m {
            for j in 0..n {
                // length of 0
                push(&mut heap, &mut seen, grid[i][j]);
                // i + 2 * x  <= m-1 => x <= (m -1- i) / 2
                // j + x <= n-1 => x <= n - 1 - j
                // j - x >= 0 => x <= j
                for l in 1..=min((m - 1 - i) / 2, min(j, n - 1 - j)) {
                    // dbg!(i, j, l);
                    let mut sum = 0;
                    let mut x = i;
                    let mut y = j;

                    // top -> right
                    for _ in 0..l {
                        sum += grid[x][y];
                        x += 1;
                        y += 1;
                    }
                    // right -> bottom
                    for _ in 0..l {
                        sum += grid[x][y];
                        x += 1;
                        y -= 1;
                    }
                    // bottom -> left
                    for _ in 0..l {
                        sum += grid[x][y];
                        x -= 1;
                        y -= 1;
                    }
                    // left -> top
                    for _ in 0..l {
                        sum += grid[x][y];
                        x -= 1;
                        y += 1;
                    }

                    push(&mut heap, &mut seen, sum);
                }
            }
        }

        // error version : don't maintain sorted order
        // heap.into_iter().map(|x| x.0).rev().collect()
        heap.into_sorted_vec().iter().map(|x| x.0).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let grid: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::get_biggest_three(grid).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
