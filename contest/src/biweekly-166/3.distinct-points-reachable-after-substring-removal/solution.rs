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
        let map: HashMap<char, usize> =
            HashMap::from_iter([('U', 0), ('D', 0), ('L', 1), ('R', 1)]);

        let mut cnt = vec![0; 2];

        fn update(cnt: &mut Vec<i32>, ch: char, delta: i32, map: &HashMap<char, usize>) {
            let flg = if ch == 'U' || ch == 'L' { 1 } else { -1 };
            cnt[map[&ch]] += flg * delta
        }

        for i in 0..k - 1 {
            update(&mut cnt, s[i], 1, &map);
        }

        let mut diff: HashSet<Vec<i32>> = HashSet::new();
        for i in k - 1..s.len() {
            update(&mut cnt, s[i], 1, &map);
            diff.insert(cnt.clone());
            update(&mut cnt, s[i - (k - 1)], -1, &map);
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
