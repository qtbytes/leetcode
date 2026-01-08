// Created by none at 2026/01/08 13:29
// leetgo: dev
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_dot_product(a: Vec<i32>, b: Vec<i32>) -> i32 {
        // f[i][j] =max(f[i-1][j], max(f[i-1][k-1] + a[i] * b[k] for k in 0..j) )
        //
        let m = a.len();
        let n = b.len();

        let mut f = vec![vec![i32::MIN; n + 1]; m + 1];

        for j in 0..n {
            f[1][j + 1] = max(f[1][j], a[0] * b[j])
        }

        // println!("{:?}", f);
        for i in 1..m {
            let mut h = BinaryHeap::new();
            for j in 0..n {
                f[i + 1][j + 1] = max(a[i] * b[j], max(f[i][j + 1], f[i + 1][j]));
                h.push(f[i][j].saturating_add(a[i] * b[j]));
                f[i + 1][j + 1] = max(f[i + 1][j + 1], *h.peek().unwrap());
            }
            // println!("{:?}", &f[..=i + 1]);
        }

        f[m][n]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums1: Vec<i32> = deserialize(&read_line()?)?;
    let nums2: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_dot_product(nums1, nums2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
