// Created by none at 2025/07/19 12:43
// leetgo: dev
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        let seen: HashSet<String> = HashSet::from_iter(folder.clone().into_iter());

        pub fn valid(s: &String, seen: &HashSet<String>) -> bool {
            let mut p = String::new();
            for ch in s.chars() {
                if ch == '/' && seen.contains(&p) {
                    return false;
                }
                p.push(ch);
            }
            true
        }

        folder.into_iter().filter(|f| valid(f, &seen)).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let folder: Vec<String> = deserialize(&read_line()?)?;
    let ans: Vec<String> = Solution::remove_subfolders(folder).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
