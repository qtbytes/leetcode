// Created by none at 2025/08/02 11:29
// leetgo: dev
// https://leetcode.com/problems/rearranging-fruits/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for &x in &basket1 {
            *cnt.entry(x).or_insert(0) += 1;
        }
        for &x in &basket2 {
            *cnt.entry(x).or_insert(0) -= 1;
        }

        let mut smallest = i32::MAX;
        let mut pairs = vec![];
        for (&k, &v) in &cnt {
            smallest = smallest.min(k);
            if v & 1 == 1 {
                return -1;
            }
            pairs.extend(vec![k; (v.abs() as usize) / 2]);
        }
        pairs.sort_unstable();

        let mut res = 0_i64;
        let mut i = 0;
        let mut j = pairs.len();
        while i < j {
            // we have 2 ways
            if pairs[i] <= smallest * 2 {
                // first, change with the dismatched fruits directly
                res += pairs[i] as i64;
            } else {
                res += smallest as i64 * 2;
                // second, change with smallest, then change with smallest again
            }
            i += 1;
            j -= 1;
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let basket1: Vec<i32> = deserialize(&read_line()?)?;
    let basket2: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::min_cost(basket1, basket2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
