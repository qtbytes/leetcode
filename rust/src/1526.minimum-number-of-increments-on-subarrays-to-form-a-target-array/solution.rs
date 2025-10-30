// Created by none at 2025/10/30 10:16
// leetgo: dev
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_number_operations(target: Vec<i32>) -> i32 {
        let n = target.len();
        let mut i = 0;
        let mut res = 0;
        let mut st = vec![];

        while i < n {
            // find sub array first inc then dec
            let mut j = i + 1;
            while j < n && target[j] >= target[j - 1] {
                j += 1
            }
            st.push(target[j - 1]);
            while j < n && target[j] <= target[j - 1] {
                j += 1
            }
            let last = st.pop().unwrap();
            res += last - target[j - 1];
            st.push(target[j - 1]);
            i = j;
        }
        res + *st.last().unwrap()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let target: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_number_operations(target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
