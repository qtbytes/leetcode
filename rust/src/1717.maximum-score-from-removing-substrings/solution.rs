// Created by none at 2025/07/23 13:04
// leetgo: dev
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

#[derive(Ord, PartialOrd, Eq, PartialEq)]
struct Operation {
    score: i32,
    pattern: String,
}

impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        let mut q = vec![
            Operation {
                score: x,
                pattern: "ab".to_string(),
            },
            Operation {
                score: y,
                pattern: "ba".to_string(),
            },
        ];
        q.sort_unstable();
        q.reverse();

        fn do_operation(s: String, o: &Operation, res: &mut i32) -> String {
            let mut st = String::new();

            for ch in s.chars() {
                st.push(ch);
                let n = st.len();
                if n >= 2 && st[n - 2..].to_string() == o.pattern {
                    *res += o.score;
                    st.pop();
                    st.pop();
                }
            }
            String::from(st)
        }
        let mut res = 0;
        let s = do_operation(s, &q[0], &mut res);
        do_operation(s, &q[1], &mut res);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let x: i32 = deserialize(&read_line()?)?;
    let y: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximum_gain(s, x, y).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
