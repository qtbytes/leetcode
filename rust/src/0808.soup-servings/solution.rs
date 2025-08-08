// Created by none at 2025/08/08 10:25
// leetgo: dev
// https://leetcode.com/problems/soup-servings/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 5e3 as i32 {
            return 1.0;
        }

        fn dfs(a: i32, b: i32, memo: &mut HashMap<(i32, i32), f64>) -> f64 {
            if a <= 0 || b <= 0 {
                if a <= 0 && b <= 0 {
                    return 0.5;
                } else if b <= 0 {
                    return 0.0;
                }
                return 1.0;
            }
            if let Some(res) = memo.get(&(a, b)) {
                return *res;
            }

            let res = dfs(a - 100, b, memo)
                + dfs(a - 75, b - 25, memo)
                + dfs(a - 50, b - 50, memo)
                + dfs(a - 25, b - 75, memo);
            memo.insert((a, b), res / 4.0);
            res / 4.0
        }
        let mut memo = HashMap::new();
        // let n = 5e3 as i32;
        // println!("{}", dfs(n, n, &mut memo));
        dfs(n, n, &mut memo)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: f64 = Solution::soup_servings(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
