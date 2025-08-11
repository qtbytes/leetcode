// Created by none at 2025/08/11 12:42
// leetgo: dev
// https://leetcode.com/problems/range-product-queries-of-powers/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

const MOD: i64 = 1e9 as i64 + 7;
impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut bits = vec![];
        for i in 0..31 {
            if n >> i & 1 != 0 {
                bits.push(1 << i);
            }
        }
        fn calc(l: usize, r: usize, bits: &Vec<i32>) -> i32 {
            let mut res = 1_i64;
            for i in l..=r {
                res = res * (bits[i] as i64) % MOD;
            }
            res as i32
        }
        queries
            .into_iter()
            .map(|q| calc(q[0] as usize, q[1] as usize, &bits))
            .collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let queries: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::product_queries(n, queries).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
