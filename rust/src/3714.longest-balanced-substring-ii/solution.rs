// Created by none at 2026/02/13 19:42
// leetgo: dev
// https://leetcode.com/problems/longest-balanced-substring-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

use std::arch::x86_64::_mm_dpbf16_ps;
// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

fn handle_one(a: &[u8]) -> i32 {
    // only one char
    let mut res = 0;
    let n = a.len();
    let mut cnt = 1;
    for i in 1..n {
        if a[i] == a[i - 1] {
            cnt += 1
        } else {
            res = max(res, cnt);
            cnt = 1
        }
    }
    max(res, cnt)
}

fn handle_two(a: &[u8], x: u8, y: u8) -> i32 {
    // two char, map a to 1, b to -1, c to 0
    let mut res = 0;
    let mut map = HashMap::new();
    map.insert(0, -1);
    let mut bal = 0;
    for i in 0..a.len() {
        let ch = a[i];
        if ch != x && ch != y {
            map.clear();
            bal = 0;
            map.insert(0, i as i32);
        } else if ch == x {
            bal += 1;
        } else {
            bal -= 1;
        }
        if let Some(j) = map.get(&bal) {
            res = max(res, i as i32 - j)
        } else {
            map.insert(bal, i as i32);
        }
    }
    res
}

fn hanlde_three(a: &[u8]) -> i32 {
    let mut res = 0;
    let mut cnt = vec![0; 3];
    let mut map = HashMap::new();
    map.insert((0, 0), -1);
    for (i, ch) in a.iter().map(|x| (x - b'a') as usize).enumerate() {
        cnt[ch] += 1;
        if let Some(j) = map.get(&(cnt[1] - cnt[0], cnt[2] - cnt[1])) {
            res = max(res, i as i32 - j)
        } else {
            map.insert((cnt[1] - cnt[0], cnt[2] - cnt[1]), i as i32);
        }
    }
    res
}
impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let a = s.as_bytes();
        let mut res = handle_one(a);

        for x in b'a'..=b'c' {
            for y in x + 1..=b'c' {
                res = max(res, handle_two(a, x, y));
            }
        }

        max(res, hanlde_three(a))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::longest_balanced(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
