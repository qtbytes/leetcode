// Created by none at 2026/01/11 13:51
// leetgo: dev
// https://leetcode.com/problems/maximal-rectangle/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn max_area(nums: &Vec<i32>) -> i32 {
    // 4 2 3 1 4 0 9 9 9
    // find the first less than a[i] for (i..0) and (i..n)

    let mut st = vec![];
    let n = nums.len();
    let mut left = vec![0; n];
    let mut right = vec![n - 1; n];

    for i in 0..n {
        while let Some(&j) = st.last() {
            if nums[i] <= nums[j] {
                right[j] = i - 1;
                st.pop();
            } else {
                break;
            }
        }
        if let Some(&j) = st.last() {
            left[i] = j + 1
        }
        st.push(i);
    }

    (0..n)
        .map(|i| nums[i] * (right[i] - left[i] + 1) as i32)
        .max()
        .unwrap()
}

impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        // for each row, zip matrix[:row] to a single row like: 4 2 3 1 4 0 9 9 9
        let mut ans = 0;
        let mut nums = vec![0; matrix[0].len()];

        for row in matrix {
            for (i, x) in row.into_iter().enumerate() {
                if x == '0' { nums[i] = 0 } else { nums[i] += 1 }
            }
            ans = max(ans, max_area(&nums))
        }

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let matrix: Vec<Vec<char>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximal_rectangle(matrix).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
