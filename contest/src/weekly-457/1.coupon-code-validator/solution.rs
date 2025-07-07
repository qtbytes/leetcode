// Created by none at 2025/07/07 17:28
// leetgo: dev
// https://leetcode.com/problems/coupon-code-validator/
// https://leetcode.com/contest/weekly-contest-457/problems/coupon-code-validator/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::collections::HashSet;

impl Solution {
    pub fn validate_coupons(
        code: Vec<String>,
        business_line: Vec<String>,
        is_active: Vec<bool>,
    ) -> Vec<String> {
        let catagories: HashSet<&str> =
            HashSet::from_iter(["electronics", "grocery", "pharmacy", "restaurant"]);

        fn valid(s: &str) -> bool {
            for ch in s.chars() {
                if !(ch.is_alphanumeric() || ch == '_') {
                    return false;
                }
            }
            true
        }

        let n = code.len();
        let mut a = vec![];
        for i in 0..n {
            if is_active[i]
                && catagories.contains(&business_line[i].as_str())
                && !code[i].is_empty()
                && valid(&code[i])
            {
                a.push(i);
            }
        }
        a.sort_unstable_by_key(|&i| (&business_line[i], &code[i]));

        a.into_iter().map(|i| code[i].to_string()).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let code: Vec<String> = deserialize(&read_line()?)?;
    let business_line: Vec<String> = deserialize(&read_line()?)?;
    let is_active: Vec<bool> = deserialize(&read_line()?)?;
    let ans: Vec<String> = Solution::validate_coupons(code, business_line, is_active).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
