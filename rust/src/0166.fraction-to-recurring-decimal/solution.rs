// Created by none at 2025/09/24 12:35
// leetgo: dev
// https://leetcode.com/problems/fraction-to-recurring-decimal/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        let (mut a, mut b) = (numerator as i64, denominator as i64);
        if a == 0 {
            return "0".to_string();
        }
        let mut res: Vec<char> = vec![];
        // handle positive
        if a * b < 0 {
            res.push('-');
        }
        (a, b) = (a.abs(), b.abs());
        res.extend((a / b).to_string().chars());
        if a % b == 0 {
            return res.into_iter().collect();
        }
        a = a % b * 10;
        res.push('.');
        // try find circle
        let mut seen = HashMap::new();
        seen.insert(a, res.len());

        while a != 0 {
            let y = a / b;
            a = (a % b) * 10;
            res.push(y.to_string().chars().next().unwrap());
            if let Some(&j) = seen.get(&a) {
                return res[..j].into_iter().collect::<String>()
                    + &format!("({})", (res[j..]).into_iter().collect::<String>());
            }
            seen.insert(a, res.len());
        }

        res.into_iter().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let numerator: i32 = deserialize(&read_line()?)?;
    let denominator: i32 = deserialize(&read_line()?)?;
    let ans: String = Solution::fraction_to_decimal(numerator, denominator).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
