// Created by none at 2025/08/04 12:04
// leetgo: dev
// https://leetcode.com/problems/fruit-into-baskets/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut cnt = HashMap::new();
        let n = fruits.len();
        let mut res = 0;
        let mut r = 0;
        for l in 0..n {
            while r < n && (cnt.len() < 2 || cnt.len() == 2 && cnt.contains_key(&fruits[r])) {
                *cnt.entry(fruits[r]).or_insert(0) += 1;
                r += 1;
            }
            res = res.max((r - l) as i32);
            if r == n {
                break;
            }
            *cnt.get_mut(&fruits[l]).unwrap() -= 1;
            if cnt[&fruits[l]] == 0 {
                cnt.remove(&fruits[l]);
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let fruits: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::total_fruit(fruits).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
