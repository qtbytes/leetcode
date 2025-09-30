// Created by none at 2025/09/30 21:53
// leetgo: dev
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/
// https://leetcode.com/contest/biweekly-contest-166/problems/distinct-points-reachable-after-substring-removal/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn distinct_points(s: String, k: i32) -> i32 {
        let k = k as usize;
        let s: Vec<char> = s.chars().collect();
        let mut cnt: HashMap<char, i32> = HashMap::new();

        fn update(cnt: &mut HashMap<char, i32>, ch: char, mut delta: i32) {
            if ch == 'U' || ch == 'D' {
                if ch == 'D' {
                    delta *= -1;
                }
                *cnt.entry('U').or_default() += delta;
                return;
            }
            if ch == 'R' {
                delta *= -1;
            }
            *cnt.entry('L').or_default() += delta
        }

        for i in 0..k - 1 {
            update(&mut cnt, s[i], 1);
        }

        let mut diff: HashSet<Vec<(char, i32)>> = HashSet::new();
        for i in k - 1..s.len() {
            update(&mut cnt, s[i], 1);
            diff.insert(cnt.clone().into_iter().filter(|i| i.1 != 0).collect());
            update(&mut cnt, s[i - (k - 1)], -1);
        }
        // println!("{diff:?}");

        diff.len() as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::distinct_points(s, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
