// Created by none at 2026/02/26 12:44
// leetgo: dev
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_steps(s: String) -> i32 {
        // 1101
        // 1110
        // 111
        // 1000
        // 100
        // 10
        // 1
        let a = s.as_bytes();
        let mut carry = 0;
        let mut res = 0;
        for i in (0..a.len()).rev() {
            let x = a[i] - b'0' + carry;
            // odd
            if x == 1 {
                // became 1
                if i == 0 {
                    break;
                }
                // add 1, divide 2
                res += 2;
                carry = 1;
            } else {
                // divide 2
                res += 1;
                carry = x / 2;
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_steps(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
