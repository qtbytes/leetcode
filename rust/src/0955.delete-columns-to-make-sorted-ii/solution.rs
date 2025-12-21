// Created by none at 2025/12/21 12:39
// leetgo: dev
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
use std::path::is_separator;

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let m = strs.len();
        let n = strs[0].len();

        let mut ans = 0;
        let mut is_larger = vec![false; m];

        for j in 0..n {
            let mut need_delete = false;
            for i in 1..m {
                if is_larger[i] {
                    continue;
                }
                if strs[i].get(j..j + 1) < strs[i - 1].get(j..j + 1) {
                    need_delete = true;
                    break;
                }
            }
            if !need_delete {
                for i in 1..m {
                    is_larger[i] |= strs[i].get(j..j + 1) > strs[i - 1].get(j..j + 1)
                }
            } else {
                ans += 1
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let strs: Vec<String> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_deletion_size(strs).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
