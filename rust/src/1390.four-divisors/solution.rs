// Created by none at 2026/01/04 13:14
// leetgo: dev
// https://leetcode.com/problems/four-divisors/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn check(x: i32) -> (bool, i32) {
    let mut cnt = 2;
    let mut sum = 1 + x; // 1 * x == x
    let mut i = 2;
    while i * i <= x {
        if x % i == 0 {
            sum += i;
            sum += x / i;
            cnt += 2;
            if x / i == i {
                cnt -= 1;
            }
            if cnt > 4 {
                break;
            }
        }
        i += 1
    }
    if cnt == 4 { (true, sum) } else { (false, 0) }
}
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut seen = HashMap::with_capacity(nums.len());

        for x in nums {
            if !seen.contains_key(&x) {
                seen.insert(x, check(x));
            }
            if let Some(&(ok, sum)) = seen.get(&x)
                && ok
            {
                ans += sum
            }
        }

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::sum_four_divisors(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
