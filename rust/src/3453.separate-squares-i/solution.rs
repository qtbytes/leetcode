// Created by none at 2026/01/13 19:09
// leetgo: dev
// https://leetcode.com/problems/separate-squares-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut l: f64 = 0.0;
        let mut r: f64 = 1e9;

        while r - l > 1e-6 {
            let mid = (l + r) / 2.0;
            let check = |mid: f64| -> bool {
                let mut ans = 0.0;
                for s in &squares {
                    let y = s[1] as f64;
                    let l = s[2] as f64;
                    let area = l * l;
                    if y + l <= mid {
                        ans -= area
                    } else if y >= mid {
                        ans += area
                    } else {
                        //(x+l-mid)/l - (mid-x)/l = (x*2+l-mid*2)/l
                        ans += area * (y * 2.0 + l - mid * 2.0) / l
                    }
                }
                ans <= 1e-5
            };
            if check(mid) { r = mid } else { l = mid + 1e-9 }
        }

        r
    }
}

// @lc code=end

fn main() -> Result<()> {
    let squares: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: f64 = Solution::separate_squares(squares).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
