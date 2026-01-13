// Created by none at 2026/01/13 19:09
// leetgo: dev
// https://leetcode.com/problems/separate-squares-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut diff = HashMap::new();
        let mut total: i64 = 0;

        for s in &squares {
            let y = s[1];
            let l = s[2];
            *diff.entry(y).or_insert(0) += l;
            *diff.entry(y + l).or_insert(0) -= l;
            total += (l as i64) * (l as i64)
        }

        let mut keys: Vec<i32> = diff.keys().cloned().collect();
        keys.sort_unstable();

        let mut sum_x = 0;
        let mut area = 0;

        for w in keys.windows(2) {
            let y1 = w[0];
            let y2 = w[1];
            sum_x += diff[&y1];
            area += sum_x as i64 * (y2 - y1) as i64;
            if area * 2 >= total {
                // (area - (y2-y) * sum_x) * 2 == total
                // (total / 2 - area) / sum_x + y2
                return y2 as f64 + (total as f64 / 2.0 - area as f64) / sum_x as f64;
            }
        }

        unreachable!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let squares: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: f64 = Solution::separate_squares(squares).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
