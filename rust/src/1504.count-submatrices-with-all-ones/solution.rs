// Created by none at 2025/08/21 13:11
// leetgo: dev
// https://leetcode.com/problems/count-submatrices-with-all-ones/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn num_submat(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat[0].len();
        let mut row = vec![0; n];
        let mut res = 0;

        fn calc(row: &Vec<i32>) -> i32 {
            let n = row.len();
            let mut left = vec![0; n];
            let mut right = vec![n - 1; n];
            let mut st = vec![];

            for i in 0..n {
                while let Some(&j) = st.last() {
                    if row[i] <= row[j] {
                        right[j] = i - 1;
                        st.pop();
                    } else {
                        left[i] = j + 1;
                        break;
                    }
                }
                st.push(i);
            }
            let mut res = 0;
            for i in 0..n {
                assert!(right[i] >= left[i]);
                // wrong: res += row[i] * (right[i] + 1 - left[i]) as i32
                res += row[i] * (i - left[i] + 1) as i32 * (right[i] - i + 1) as i32;
            }
            // println!("{:?} {:?} {:?} {res}", row, left, right);
            res
        }

        for each_row in mat {
            for (i, x) in each_row.into_iter().enumerate() {
                if x == 0 { row[i] = 0 } else { row[i] += 1 }
            }
            res += calc(&row);
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mat: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_submat(mat).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
