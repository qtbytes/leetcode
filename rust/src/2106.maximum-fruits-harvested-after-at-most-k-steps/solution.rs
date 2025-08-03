// Created by none at 2025/08/03 12:04
// leetgo: dev
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        let n = fruits.len();
        let mut position = vec![0; n];
        let mut amount = vec![0; n];
        let mut prefix = vec![0; n + 1];
        for (i, f) in fruits.into_iter().enumerate() {
            position[i] = f[0];
            amount[i] = f[1];
            prefix[i + 1] = prefix[i] + f[1];
        }
        let mut res = 0;
        // p[mid] > start
        let mut mid = position.partition_point(|&p| p <= start_pos);
        if mid > 0 {
            // l..mid
            let l = position.partition_point(|&p| p < start_pos - k);
            if l <= mid {
                res = res.max(prefix[mid] - prefix[l]);
            }
        }
        // mid..r
        if mid > 0 && position[mid - 1] == start_pos {
            mid -= 1;
        }
        let r = position.partition_point(|&p| p <= start_pos + k);
        res = res.max(prefix[r] - prefix[mid]);
        // println!("{res}");

        for (r, &p) in position.iter().enumerate() {
            if p <= start_pos {
            } else if p - start_pos > k {
                break;
            } else {
                // start -> l -> r
                // start - p[l] + p[r] - p[l] <= k
                let target = start_pos + p - k;
                let l = position.partition_point(|p| 2 * p < target);
                if position[l] < start_pos && l <= r {
                    res = res.max(prefix[r + 1] - prefix[l]);
                }

                // start -> r -> l
                // (p[r] - start + p[r] - p[l] <= k
                let target = 2 * p - start_pos - k;
                let l = position.partition_point(|&p| p < target);
                if l <= r {
                    res = res.max(prefix[r + 1] - prefix[l]);
                }
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let fruits: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let start_pos: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_total_fruits(fruits, start_pos, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
